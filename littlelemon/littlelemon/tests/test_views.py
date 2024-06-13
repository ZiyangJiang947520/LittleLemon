from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Cake", price=150, inventory=50)

    def test_get_all(self):
        response = self.client.get(reverse('menu-items'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
