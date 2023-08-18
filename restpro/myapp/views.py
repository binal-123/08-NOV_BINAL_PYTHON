from django.shortcuts import render
from .models import book
from .serializers import bookserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def getall(request):
    if request.method=="GET":
    
        stid=book.objects.all()
        serial=bookserializer(stid,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookserializer(stid)
    return Response(serial.data,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteid(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        book.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=bookserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookserializer(stid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method=='PUT':
        serial=bookserializer(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)