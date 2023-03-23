from .models import PasswordManager
from .serializers import PwdSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class PasswordsAPI(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        all_pwds = PasswordManager.objects.filter(user = request.user.id)
        pwd_serialized = PwdSerializer(all_pwds, many=True)
        return Response(pwd_serialized.data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        pwd_serialized = PwdSerializer(data=request.data)
        if pwd_serialized.is_valid():
            pwd_serialized.save()
            return Response(pwd_serialized.data)
        return Response(pwd_serialized.errors)
    
    def patch(self, request):
        pwd = PasswordManager.objects.get(id = request.data['id'])
        pwd_serialized = PwdSerializer(pwd, data=request.data, partial=True)
        if pwd_serialized.is_valid():
            pwd_serialized.save()
            return Response(pwd_serialized.data)
        return Response(pwd_serialized.errors)
    
    def delete(self, request):
        pwd = PasswordManager.objects.get(id = request.data['id'])
        pwd.delete()
        return Response({"info":"deleted"})
        
    
