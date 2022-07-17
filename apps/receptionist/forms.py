from django.contrib.auth.forms import UserCreationForm
from ..hospital.models import User

class ReceptionistSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_receptionist = True
        if commit:
            user.save()
        return user