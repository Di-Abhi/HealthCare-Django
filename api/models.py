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
    

class Appointment (models.Model):
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    assigned_by=models.ForeignKey(User,related_name='assigned_appointments', on_delete=models.CASCADE)
    reason = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('patient', 'doctor', 'appointment_date')

    def __str__(self):
        return f"Appointment {self.id} - Patient: {self.patient.name}, Doctor: {self.doctor.name} on {self.appointment_date}"