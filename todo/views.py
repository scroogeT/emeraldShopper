from django.views import generic
from todo.models import ShoppingItem


class CreateShoppingItem(generic.CreateView):
    model = ShoppingItem
    fields = '__all__'
    success_url = '/'


class ShoppingItems(generic.ListView):
    model = ShoppingItem
    context_object_name = 'shopping_items'


class EditShoppingItem(generic.UpdateView):
    model = ShoppingItem
    context_object_name = 'shopping_item'
    fields = '__all__'
    success_url = '/'


class DeleteShoppingItem(generic.DeleteView):
    model = ShoppingItem
    success_url = '/'
