from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
#django is a package . Shortcut is a module
# #and were importing the render function

from rest_framework.response import Response
from .serializers import CarSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['ORDER-CAR'])
def order_car(request, customerId, carId):
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        if Car.status == "available":
            Car.status = "booked"
        else:
            return "car unavailable"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
# we need to connect this URL: /cars to this function (index)
#UML - uniform resource locator (address)
#YT video 5.49.30

def index(request):
    Cars = Car.objects.all()
    return render(request, "index.html", {"Cars": Cars})


def new(request):
    return HttpResponse("New Cars")

