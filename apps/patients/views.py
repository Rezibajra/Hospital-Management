from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm


def view_patient(request):
    patients = Patient.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {'patients': patients}
    return render(request, 'patients/view_patient.html', context)

def add_patient(request):
    form = PatientForm()
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        Patient.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address'),
            gender = request.POST.get('gender'),
        )
        return redirect('view_patient')
    context = {'form': form}
    return render(request, 'patients/patient_form.html', context)
    
def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.address = request.POST.get('address')
        patient.gender = request.POST.get('gender')
        patient.save()
        return redirect('view_patient')
    context = {'form': form, 'patient': patient}
    return render(request, 'patients/patient_form.html', context)

def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        patient.delete()
        return redirect('view_patient')

    context = {'obj': patient}
    return render(request, 'hospital/delete.html', context)
