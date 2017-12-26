from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):

    def get(self,request):
        return Response(['hello', 'world'])

    def post(self,request):
        return Response(request.data) # en rest_framework los datos que me envian `
                                      # siempre se accede desde la varialbe `data