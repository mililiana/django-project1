from tokenize import Token

from django.contrib.auth import logout
from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Item, OrderItem
import requests
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Item, OrderItem
from .serializers import UserSerializer, ItemSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response




from .serializers import UserSerializer, ItemSerializer, OrderItemSerializer


from rest_framework.decorators import api_view





def  homepage(request):
    return render(request, 'homepage.html')

def  homepage1(request):
    return render(request, 'homepage1.html')
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

@api_view(['POST'])

def logout_user(request):
    if request.method == 'POST':
        request.user.auth_tocken.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, id, format=None):
    print(f"Received user ID: {id}")
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        print(f"User with ID {id} not found.")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = UserSerializer(user, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_user(request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update your items_list view
@api_view(['GET', 'POST'])
def items_list(request, format=None):
    if request.method == "GET":
        items = Item.objects.all()
        return render(request, 'items_list.html', {'items': items})
    elif request.method == "POST":
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ajax_items_list(request):
    items = Item.objects.all()
    html_content = render_to_string('items_list.html', {'items': items})
    return JsonResponse({'html_content': html_content, 'items': list(items)})


@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})
@api_view(['POST'])
def create_item(request, format=None):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def order_items_list(request, format=None):
    if request.method == "GET":
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_items_detail(request, id, format=None):
    try:
        order_item = OrderItem.objects.get(pk=id)
    except OrderItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_order_item(request, format=None):
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_orders(request, id,format=None):
    orders = OrderItem.objects.filter(user=id)
    serializer = OrderItemSerializer(orders, many = True)
    return Response(serializer.data)



