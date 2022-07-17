from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Doctor
from ..hospital.models import User

class DoctorSignUpForm(UserCreationForm):
    address = forms.CharField(max_length=50)
    speciality = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.address = self.cleaned_data.get('address')
        doctor.speciality = self.cleaned_data.get('speciality')
        doctor.save()
        return user