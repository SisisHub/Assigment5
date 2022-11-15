from .models import Employee
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

@api_view(['GET'])
def get_employee(request):
    employees = Employees.objects.all()
    serializer = EmployeeSerializer(Employee, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theEmployee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        theEmployee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theEmployee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    employee = Employee.objects.all()
    return render(request, "index.html", {"employee": employee})


def new(request):
    return HttpResponse("New client")