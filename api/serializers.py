from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    name = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ("username", "name", "email", "password")
        extra_kwargs = {
            "username": {"required": True},
        }

    def create(self, validated_data): 
        username = validated_data["username"]
        password = validated_data["password"]
        email = validated_data["email"]
        name = validated_data.get("name", "")

        user = User.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        if name:
            user.first_name = name  
        user.save()
        return user

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    name = serializers.CharField(write_only=True,required=False,allow_blank=True)

    class Meta:
        model = User
        fields = ("username","name","email", "password")
        extra_kwargs = {
            'username': {'required': True},
        }

        def create(self, validated_data):
            username = validated_data["username"]
            password = validated_data["password"]
            email = validated_data["email"]
            name = validated_data.get("name", "")

            user = User.objects.create(
                username=username,
                email=email,
            )
            user.set_password(password)
            if name:
                user.first_name = name
            user.save()
            return user
class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']

class AppointmentSerializer(serializers.ModelSerializer):
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)

    class Meta:
        model = Appointment
        fields = (
            "id", "patient", "patient_details", "doctor", "doctor_details",
            "appointment_date", "reason", "assigned_by", "created_at", "updated_at"
        )
        read_only_fields = ("id", "created_at", "updated_at")
