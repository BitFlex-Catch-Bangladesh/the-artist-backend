from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
from .models import *
from .serializer import *
import datetime
import base64
from django.core.files.base import ContentFile


@api_view(['GET'])
def getHomeBanner(request):
    stored_data = HomeBanner.objects.all()
    serializer = HomeBannerSerializer(stored_data, many=True)
    return Response(serializer.data[0])


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addHomeBanner(request):
    try:
        payload = request.data
        if 'image1' in payload:
            fmt, img_str = str(payload['image1']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['image1'] = img_file
        if 'image2' in payload:
            fmt, img_str = str(payload['image2']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['image2'] = img_file
        if 'image3' in payload:
            fmt, img_str = str(payload['image3']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['image3'] = img_file
        if 'image4' in payload:
            fmt, img_str = str(payload['image4']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['image4'] = img_file

        homeBanner_instance = HomeBanner.objects.all()
        print(homeBanner_instance)
        print(len(homeBanner_instance)==0)

        if len(homeBanner_instance) == 0:
            print("add")
            homeBanner_serializer = HomeBannerSerializer(data=payload)
            if homeBanner_serializer.is_valid():
                homeBanner_serializer.save()
                response = {
                    'code': '200',
                    'data': HomeBannerSerializer(homeBanner_serializer.instance, context={'request': request}).data
                }
                return Response(response)
            else:
                return Response(homeBanner_serializer.errors)
        else:
            print("update")
            homeBanner_serializer = HomeBannerSerializer(instance=homeBanner_instance[0], data=payload)
            if homeBanner_serializer.is_valid():
                homeBanner_serializer.save()
                response = {
                    'code': '200',
                    'data': HomeBannerSerializer(homeBanner_serializer.instance, context={'request': request}).data
                }
                return Response(response)
            else:
                return Response(homeBanner_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)
