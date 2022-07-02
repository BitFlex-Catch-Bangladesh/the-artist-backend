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
def getImage(request):
    stored_data = Image.objects.all()
    serializer = ImageSerializer(stored_data, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addImage(request):
    try:
        payload = request.data
        if 'img' in payload:
            fmt, img_str = str(payload['img']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['img'] = img_file

        image_serializer = ImageSerializer(data=payload)
        if image_serializer.is_valid():
            image_serializer.save()
            response = {
                'code': '200',
                'data': ImageSerializer(image_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(image_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteImage(request,pk):

    stored_data = Image.objects.get(id=pk)
    stored_data.delete()
    return Response({'msg': "Item Deleted Successfully!"})
