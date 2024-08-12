from django.urls import path
from .views import index, contact_view


app_name='core'
urlpatterns = [
    path('', index, name='index'),  
    path('create/', contact_view, name='contact_view'),  
]
