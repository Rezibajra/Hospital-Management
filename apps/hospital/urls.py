from django.urls import path
from .views import home, login_page, logout_page

urlpatterns = [
    path('', home, name='home'),
    path('admin_login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]