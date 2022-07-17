from django.urls import path
from .views import view_appointment, add_appointment, delete_appointment

urlpatterns = [
    path('view_appointment/', view_appointment, name='view_appointment'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('delete_appointment/<int:pk>/', delete_appointment, name='delete_appointment'),
]