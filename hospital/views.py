from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment
from .forms import PatientForm, AppointmentForm

from .models import Patient
from .forms import PatientForm


def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

        else:
            error = "Invalid Username or Password"

    return render(request, 'hospital/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):

    total_patients = Patient.objects.count()

    return render(request, 'hospital/dashboard.html', {
        'total_patients': total_patients
    })


@login_required
def add_patient(request):

    form = PatientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'hospital/add_patient.html', {
        'form': form
    })


@login_required
def patient_list(request):

    query = request.GET.get('q')

    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()

    return render(request, 'hospital/patient_list.html', {
        'patients': patients
    })

@login_required
def edit_patient(request, id):

    patient = get_object_or_404(Patient, id=id)

    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'hospital/edit_patient.html', {
        'form': form
    })


@login_required
def delete_patient(request, id):

    patient = get_object_or_404(Patient, id=id)

    patient.delete()

    return redirect('patient_list')

@login_required
def add_appointment(request):

    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'hospital/add_appointment.html', {
        'form': form
    })