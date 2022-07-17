from django.urls import path
from .views import ReceptionistSignUpView

urlpatterns = [
    path('accounts/signup/', ReceptionistSignUpView.as_view(), name='receptionist_signup')
]