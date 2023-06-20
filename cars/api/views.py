from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import car_details
from .serializer import carserializer,mainserializer
from rest_framework import status
from .forms import carform
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response("helo world")


@api_view(['GET'])
def getmain(request):
    cars=car_details.objects.all()
    serializer=carserializer(cars,many=True)
    return Response(serializer.data)    


@api_view(['GET','DELETE'])
def getcar(request,pk):
    if request.method=='GET':
        cars=car_details.objects.get(id=pk)
        serializer=mainserializer(cars,many=False)
        return Response(serializer.data)
    
    if request.method=='DELETE':
        cars=car_details.objects.get(id=pk)
        cars.delete()
        return Response("deleted")
    
@api_view(['POST'])
def postcar(requst):
    serializer=mainserializer(data=requst.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_protect
def formpage(request):
    form = carform()
    if request.method == "POST":
        form = carform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = carform()

    return render(request, "index.html", {'form': form})