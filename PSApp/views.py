from django.shortcuts import render

from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import contests
from .serializers import contestsSerializer
import jwt,json

# Create your views here.
class problem_solution(APIView):


    def post(self,request):
    #JWT
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        username = request.data['username']
        password = request.data['password']

        try:
            user = contests.objects.get(username=username, password=password)
        except contests.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")

        # Serializer
        contests1=contests.objects.all()
        serializer=contestsSerializer(contests1, many=True)
        return Response(serializer.data)

    def get(self):
        pass

