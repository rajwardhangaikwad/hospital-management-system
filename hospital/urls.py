from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('add-patient/', views.add_patient, name='add_patient'),

    path('patients/', views.patient_list, name='patient_list'),

    path('edit-patient/<int:id>/', views.edit_patient, name='edit_patient'),

    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),

    path('add-appointment/', views.add_appointment, name='add_appointment'),
]