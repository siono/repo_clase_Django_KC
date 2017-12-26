from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class HelloWorld(APIView):

    def get(self,request):
        return Response(['hello', 'world'])

    def post(self,request):
        return Response(request.data) # en rest_framework los datos que me envian `
                                      # siempre se accede desde la varialbe `data


class UsersListAPI(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)