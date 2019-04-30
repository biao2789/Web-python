from django.shortcuts import render
from applications.models import App
from applications.serializers import AppSerializer
# from .forms import UploadFileForm
# from .models import ModelWithFileField

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
# 列出所有信息
class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


# 获取最新版本的信息
class AppLatest(APIView):
    def get(self, request, format=None):
        name = request.query_params.get("name")
        queryset = App.objects.filter(name=name).order_by('-id').first()
        serilizer = AppSerializer(queryset)
        return Response(serilizer.data)