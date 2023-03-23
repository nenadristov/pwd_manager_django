from django.urls import path
from .views import PasswordsAPI


urlpatterns = [ 
    path("password/", PasswordsAPI.as_view())
]