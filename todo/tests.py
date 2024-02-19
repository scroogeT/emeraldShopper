from django.urls import reverse
from django.db import IntegrityError
from django.test import TestCase, Client
from todo.models import ShoppingItem


class ShoppingItemModelTest(TestCase):
    def setUp(self):
        ShoppingItem.objects.create(name='Milk', description='Dairy', quantity=1, is_completed=False)

    def test_shopping_item_name(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        expected_object_name = f'{shopping_item.name}'
        self.assertEqual(expected_object_name, 'Milk')

    def test_shopping_item_name_empty(self):
        with self.assertRaises(IntegrityError):
            ShoppingItem.objects.create(name=None, description='Dairy', quantity=1, is_completed=False)

    def test_shopping_item_description(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        expected_object_description = f'{shopping_item.description}'
        self.assertEqual(expected_object_description, 'Dairy')

    def test_shopping_item_quantity(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        expected_object_quantity = f'{shopping_item.quantity}'
        self.assertEqual(expected_object_quantity, '1')

    def test_shopping_item_is_completed(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        expected_object_is_completed = f'{shopping_item.is_completed}'
        self.assertEqual(expected_object_is_completed, 'False')

    def test_shopping_item_created_on(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        self.assertIsNotNone(shopping_item.created_on)

    def test_shopping_item_updated_on(self):
        shopping_item = ShoppingItem.objects.get(id=1)
        self.assertIsNotNone(shopping_item.updated_on)


class TestUserView(TestCase):
    def setUp(self):
        self.client = Client()
        self.shopping_list = reverse('todo:shopping-items')
        self.create_shopping_item = reverse('todo:create-shopping-item')
        self.edit_shopping_item = reverse('todo:edit-shopping-item', args=[1])
        self.delete_shopping_item = reverse('todo:delete-shopping-item', args=[1])

    def test_shopping_list(self):
        response = self.client.get(self.shopping_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/shoppingitem_list.html')

    def test_create_shopping_item(self):
        response = self.client.get(self.create_shopping_item)
        self.assertEqual(response.status_code, 200)

    def test_edit_shopping_item(self):
        shopping_item = ShoppingItem.objects.create(name='Milk', description='Dairy', quantity=1, is_completed=False)
        self.edit_shopping_item = reverse('todo:edit-shopping-item', args=[shopping_item.id])
        response = self.client.get(self.edit_shopping_item)
        self.assertEqual(response.status_code, 200)

    def test_delete_shopping_item(self):
        shopping_item = ShoppingItem.objects.create(name='Milk', description='Dairy', quantity=1, is_completed=False)
        self.delete_shopping_item = reverse('todo:delete-shopping-item', args=[shopping_item.id])
        response = self.client.get(self.delete_shopping_item)
        self.assertEqual(response.status_code, 200)
