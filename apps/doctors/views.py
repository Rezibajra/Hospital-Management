from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

# Create your views here.
def view_doctor(request):
    doctors = Doctor.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {'doctors': doctors}
    return render(request, 'doctors/view_doctor.html', context)

def add_doctor(request):
    form = DoctorForm()
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        Doctor.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address'),
            speciality = request.POST.get('speciality'),
        )
        return redirect('view_doctor')
    context = {'form': form}
    return render(request, 'doctors/doctor_form.html', context)
    
def update_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.address = request.POST.get('address')
        doctor.speciality = request.POST.get('speciality')
        doctor.save()
        return redirect('view_doctor')
    context = {'form': form, 'doctor': doctor}
    return render(request, 'doctors/doctor_form.html', context)

def delete_doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        doctor.delete()
        return redirect('view_doctor')

    context = {'obj': doctor}
    return render(request, 'hospital/delete.html', context)