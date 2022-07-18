from django.urls import path
from .views import view_patient, add_patient, update_patient, delete_patient

urlpatterns = [
    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/', add_patient, name='add_patient'),
    path('update_patient/<int:pk>/', update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', delete_patient, name='delete_patient'),
]