from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

from .models import Customer
from .serializer import CustomerSerializer, CustomerMenuSerializer
# Create your views here.


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_menus(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id) 
    serializer = CustomerMenuSerializer(instance=customer)
    return Response(serializer.data)
