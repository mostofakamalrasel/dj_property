from django.urls import path
from pages.views import home, about

app_name = 'pages'

urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about')
]
