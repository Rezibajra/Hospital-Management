from django.shortcuts import render, redirect
from ..patients.models import Patient
from ..doctors.models import Doctor
from .models import Appointment
from .forms import AppointmentForm


def view_appointment(request):
    appointments = Appointment.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.is_doctor:
        appointments = Appointment.objects.all().filter(doctor__user = request.user)
    
    context = {'appointments': appointments}
    return render(request, 'appointment/view_appointment.html', context)

def add_appointment(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    form = AppointmentForm()
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        doctor_name = request.POST.get('doctor')
        patient_name = request.POST.get('patient')
        doctor, created = Doctor.objects.get_or_create(user__username = doctor_name)
        patient, created = Patient.objects.get_or_create(name = patient_name)

        Appointment.objects.create(
            doctor = doctor,
            patient = patient,
            date = request.POST.get('date'),
            time = request.POST.get('time'),
        )
        return redirect('view_appointment')
    context = {'form': form, 'doctors': doctors, 'patients': patients}
    return render(request, 'appointment/appointment_form.html', context)
    
def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        appointment.delete()
        return redirect('view_appointment')

    context = {'obj': appointment}

    return render(request, 'hospital/delete.html', context)