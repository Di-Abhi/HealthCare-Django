from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    created_by = models.ForeignKey(User,related_name='patients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    notes = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.id}) {self.name} - {self.speciality or 'General'}"
    

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, related_name="mappings", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="mappings", on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(User, related_name="assigned_mappings", on_delete=models.SET_NULL, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return f"Patient {self.patient_id} -> Doctor {self.doctor_id}"