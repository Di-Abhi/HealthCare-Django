from django.shortcuts import render
from rest_framework import generics,viewsets,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, Appointment
from .serializers import (RegisterSerializer,PatientSerializer, DoctorSerializer, AppointmentSerializer)
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


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("patient","doctor","assigned_by").all().order_by('-appointment_date')
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = get_object_or_404(Patient, id=serializer.validated_data['patient'].id)
        doctor = get_object_or_404(Doctor, id=serializer.validated_data['doctor'].id)

        if patient.created_by != request.user:
            return Response({"error": "You can only create appointments for your own patients."}, status=status.HTTP_403_FORBIDDEN)
        
        appointment, created = Appointment.objects.get_or_create(
            patient=patient,
            doctor=doctor,
            appointment_date=serializer.validated_data['appointment_date'],
            defaults={'assigned_by': request.user}
        )

        if not created: 
            return Response({"error": "An appointment for this patient with this doctor on this date already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        out = self.get_serializer(appointment)
        return Response(out.data, status=status.HTTP_201_CREATED)