from multiprocessing.connection import Client

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Item, OrderItem
from datetime import date

from .serializers import OrderItemSerializer


class MyAppTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='testuser', surname='testsurname', date_of_birth='1990-01-01', contact_number='1234567890')
        self.item = Item.objects.create(name='Test Item', price=10.99, size=42, color='Red')
        self.order_item = OrderItem.objects.create(date='2023-01-01', amount=2, user=self.user)
        self.order_item.items.add(self.item)

    def test_users_detail(self):
        response = self.client.get(f'/myshop1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.user.name)

    def test_create_user(self):
        data = {'name': 'newuser', 'surname': 'newsurname', 'date_of_birth': '1995-01-01', 'contact_number': '9876543210'}
        response = self.client.post('/myshop1/create_user/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_items_list(self):
        response = self.client.get('/myshop1/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ItemCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_item_url = '/create_item/'

    def test_create_item(self):
        data = {
            'name': 'Test Item',
            'price': 100,
            'size': 42,
            'color': 'Red',
        }

        response = self.client.post(self.create_item_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)

        item = Item.objects.get()
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.price, 100)
        self.assertEqual(item.size, 42)
        self.assertEqual(item.color, 'Red')


class GetUserOrdersTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Test', surname='User', date_of_birth='2000-01-01', contact_number='123456789')
        self.order_item = OrderItem.objects.create(date='2023-01-01', amount=1, user=self.user)

    def test_get_user_orders(self):
        url = f'/myshop1/users/{self.user.id}/orders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = OrderItemSerializer([self.order_item], many=True).data
        self.assertEqual(response.data, expected_data)


