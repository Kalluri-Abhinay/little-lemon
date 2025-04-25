from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_menu_item_str_representation(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        expected_str = "IceCream : 80.00"
        self.assertEqual(str(item), expected_str)