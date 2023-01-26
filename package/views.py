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
from django.utils.text import slugify
from django.core.files.base import ContentFile
from image.models import *
from review.models import *
from video.models import *
from contact.models import *


@api_view(['GET'])
def getPackages(request):
    stored_data = Package.objects.all()
    serializer = PackageSerializer(stored_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPackagesByCategory(request, pk):
    stored_data = Package.objects.filter(category=pk)
    serializer = PackageSerializer(stored_data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPackagesByID(request, pk):
    stored_data = Package.objects.get(id=pk)
    serializer = PackageSerializer(stored_data)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPackage(request):
    try:
        payload = request.data
        if 'img' in payload:
            fmt, img_str = str(payload['img']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['img'] = img_file

        package_serializer = PackageSerializer(data=payload)

        if package_serializer.is_valid():
            instance = package_serializer.save()
            print(instance.package_name)
            package_id = str(instance.id)
            package_slug = slugify(instance.package_name) + "-" + package_id
            print(package_slug)
            instance.slug = package_slug
            instance.save()

            response = {
                'code': '200',
                'data': PackageSerializer(package_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(package_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updatePackage(request, pk):
    try:
        payload = request.data
        print

        if 'img' in payload and payload['img'] != None:
            print('hello')
            fmt, img_str = str(payload['img']).split(';base64,')
            ext = fmt.split('/')[-1]
            img_file = ContentFile(base64.b64decode(img_str), name='temp.' + ext)
            payload['img'] = img_file
        package_instance = Package.objects.get(id=pk)
        package_serializer = PackageSerializer(instance=package_instance, data=payload, partial=True)

        if package_serializer.is_valid():

            package_serializer.save()
            response = {
                'code': '200',
                'data': PackageSerializer(package_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(package_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePackage(request, pk):
    stored_data = Package.objects.get(id=pk)
    stored_data.delete()
    return Response({'msg': "Item Deleted Successfully!"})


# from image.models import *
# from review.models import *
# from video.models import *
# from contact.models import *
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCounts(request):
    package_count = Package.objects.all().count()
    image_count = Image.objects.all().count()
    review_count = Review.objects.all().count()
    video_count = Video.objects.all().count()

    return Response({
        "code": 200,
        "package": package_count,
        "image": image_count,
        "review": review_count,
        "film": video_count
    })
