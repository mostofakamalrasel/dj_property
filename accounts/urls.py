from django.urls import path
from accounts.views import login, register, logout, dashboard

app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register'),
    path('dashboard', dashboard, name='dashboard')
]
