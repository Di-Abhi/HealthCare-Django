from django.shortcuts import render
from rest_framework import generics,viewsets,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (RegisterSerializer,PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer)
from .permissions import IsOwnerOrReadOnly

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class=PatientSerializer
    permission_classes=[IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):

        if(self.action=='list'):
            return Patient.objects.filter(created_by=self.request.user).order_by('-created_at')
        return Patient.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('name')
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.select_related("patient", "doctor", "assigned_by").all().order_by("-assigned_at")
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = get_object_or_404(Patient, id=serializer.validated_data["patient"].id)
        doctor = get_object_or_404(Doctor, id=serializer.validated_data["doctor"].id)

        if patient.created_by != request.user:
            return Response({"detail": "You can only assign doctors to patients you created."}, status=status.HTTP_403_FORBIDDEN)

        mapping, created = PatientDoctorMapping.objects.get_or_create(
            patient=patient, doctor=doctor, defaults={"assigned_by": request.user}
        )
        if not created:
            return Response({"detail": "This doctor is already assigned to the patient."}, status=status.HTTP_400_BAD_REQUEST)

        out = self.get_serializer(mapping)
        return Response(out.data, status=status.HTTP_201_CREATED)