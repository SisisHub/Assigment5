from .models import Customer
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

@api_view(['GET'])
def get_customer(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, id):
    try:
        theCustomer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCustomer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['CANCEL-ORDER-CAR'])
def order_car(request, customerId, carId):

    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if carId.status == "booked":
        print ("order found")
        if serializer.is_valid():
            carId.status = "available"
            serializer.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return "car is available"

@api_view(['RENT-CAR'])
def order_car(customerId, carId):
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        if theCar.status == "booked":
            theCar.status = "rented"
        else:
            return "car not booked"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['RETURN-CAR'])
def order_car(customerId, carId):
    car_stat = ['ok', 'rented', 'damaged']
    try:
        theCustomer = Customer.objects.get(pk=customerId)
        theCar = Car.objects.get(pk=carId)
    except Customer.DoesNotExist and Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCustomer, data=request.data)
    if serializer.is_valid():
        rStatus = random.choice(car_stat)
        theCar.status = rStatus
        if theCar.status == 'ok':
            theCar.status = "available"
        elif theCar.status == 'rented':
            theCar.status = "available"
        else:
            return "damaged"
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def index(request):
    customer = Customer.objects.all()
    return render(request, "index.html", {"customer": customer})


def new(request):
    return HttpResponse("new customer")