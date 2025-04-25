from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.urls import reverse

class MenuViewTest(TestCase):
    def test_setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="Pizza", Price=12.99, Inventory=5)
        self.item2 = Menu.objects.create(Title="Pasta", Price=8.50, Inventory=10)
        self.item3 = Menu.objects.create(Title="Salad", Price=6.75, Inventory=15)

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/') # Your view must be named 'menu-list'
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
