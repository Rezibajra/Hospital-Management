from django.urls import path
from .views import DoctorSignUpView

urlpatterns = [
    path('accounts/signup/', DoctorSignUpView.as_view(), name='doctor_signup'),
]