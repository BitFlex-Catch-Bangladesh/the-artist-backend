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



@api_view(['GET'])
def getVideo(request):
    stored_data = Video.objects.all()
    serializer = VideoSerializer(stored_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createVideo(request):
    try:

        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            response = {
                'code': '200',
                'message': "Film created Successfully",
                'data': VideoSerializer(video_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(video_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateVideo(request, pk):
    try:

        video_instance = Video.objects.get(id=pk)
        video_serializer = VideoSerializer(instance=video_instance,data=request.data )
        if video_serializer.is_valid():
            video_serializer.save()
            response = {
                'code': '200',

                'message': "Film updated Successfully",
                'data': VideoSerializer(video_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(video_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteVideo(request, pk):
    stored_data = Video.objects.get(id=pk)
    stored_data.delete()
    response = {
        'code': '200',
        'message': "Film Deleted Successfully!"
    }
    return Response(response)
