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
@permission_classes([IsAuthenticated])
def getContact(request):
    stored_data = Contact.objects.all()
    serializer = ContactSerializer(stored_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getContactByDetails(request,pk):
    stored_data = Contact.objects.get(id=pk)
    serializer = ContactSerializer(stored_data)
    return Response(serializer.data)
@api_view(['POST'])
def createContact(request):
    try:

        contact_serializer = ContactSerializer(data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            response = {
                'code': '200',
                'message': "Contact Created Successfully!",
                'data': ContactSerializer(contact_serializer.instance, context={'request': request}).data
            }
            return Response(response)
        else:
            return Response(contact_serializer.errors)
    except Exception as e:
        response = {
            'code': '400',
            'message': str(e)
        }
        return Response(response)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteContact(request, pk):
    stored_data = Contact.objects.get(id=pk)
    stored_data.delete()
    response = {
        'code': '200',
        'message': "Contact Deleted Successfully!"
    }
    return Response(response)
