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
def getReview(request):
    stored_data = Review.objects.all()
    serializer = ReviewSerializer(stored_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createReview(request):
    try:
        payload = request.data
        if 'img' in payload:
            fmt, img_str = str(payload['img']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['img'] = img_file

        review_serializer = ReviewSerializer(data=payload)
        if review_serializer.is_valid():
            review_serializer.save()
            response = {
                'code': '200',
                'message':"Review Created Successfully!",
                'data': ReviewSerializer(review_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(review_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateReview(request, pk):
    try:
        payload = request.data
        if 'img' in payload:
            fmt, img_str = str(payload['img']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['img'] = img_file
        review_instance = Review.objects.get(id=pk)
        review_serializer = ReviewSerializer(instance=review_instance,data=payload )
        if review_serializer.is_valid():
            review_serializer.save()
            response = {
                'code': '200',
                'message': "Review Created Successfully!",
                'data': ReviewSerializer(review_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(review_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteReview(request, pk):
    stored_data = Review.objects.get(id=pk)
    stored_data.delete()
    response = {
        'code': '200',
        'message': "Review Deleted Successfully!"
    }
    return Response(response)
