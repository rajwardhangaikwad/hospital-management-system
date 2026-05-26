from django import forms
from .models import Patient, Appointment


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control'}),

            'age': forms.NumberInput(attrs={'class':'form-control'}),

            'gender': forms.Select(
                choices=[
                    ('Male','Male'),
                    ('Female','Female')
                ],
                attrs={'class':'form-control'}
            ),

            'disease': forms.TextInput(attrs={'class':'form-control'}),

            'phone': forms.TextInput(attrs={'class':'form-control'}),

            'address': forms.Textarea(attrs={'class':'form-control'}),
        }


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {

            'patient_name': forms.TextInput(attrs={'class':'form-control'}),

            'doctor_name': forms.TextInput(attrs={'class':'form-control'}),

            'appointment_date': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'class':'form-control',
                    'type':'time'
                }
            ),
        }