from .models import PasswordManager
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class PwdSerializer(ModelSerializer):


    class Meta:
        model = PasswordManager
        fields = ["id", "title", "description", "created_at", "updated_at", "link", "password", "user"]