from django.urls import path
from contacts.views import contact

app_name = 'contacts'

urlpatterns = [
    path('', contact, name='contact')
]
