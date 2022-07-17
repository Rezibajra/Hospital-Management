from django.urls import path
from .views import home, login_page, logout_page, signup_page

urlpatterns = [
    path('', home, name='home'),
    path('admin_login/', login_page, name='login'),
    path('accounts/signup/', signup_page, name='signup'),
    path('logout/', logout_page, name='logout'),
]