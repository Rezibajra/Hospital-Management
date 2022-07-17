from django.urls import path
from .views import view_doctor, add_doctor, update_doctor, delete_doctor

urlpatterns = [
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('update_doctor/<int:pk>/', update_doctor, name='update_doctor'),
    path('delete_doctor/<int:pk>/', delete_doctor, name='delete_doctor'),
]