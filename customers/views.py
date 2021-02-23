from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializer import CustomerSerializer, CustomerMenuSerializer
# Create your views here.


@api_view(['GET'])
def list_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_menus(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id) 
    serializer = CustomerMenuSerializer(instance=customer)
    return Response(serializer.data)


@api_view(['GET'])
def menu_details(request, customer_id, menu_id):
    return Response({'Hi':'Hi'})