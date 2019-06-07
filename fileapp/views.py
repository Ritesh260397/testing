from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File
# Create your views here.

class DetailView(APIView):
    def get(self, request):
        check=File.objects.all()
        detail = FileSerializer(check,many=True)
        return Response(detail.data,status=status.HTTP_201_CREATED)
