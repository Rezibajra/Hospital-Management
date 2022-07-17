from django.forms import ModelForm
from django import forms
from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }