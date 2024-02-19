from django.views import generic
from todo.models import ShoppingItem


class CreateShoppingItem(generic.CreateView):
    model = ShoppingItem
    fields = '__all__'
    success_url = '/'


class ShoppingItems(generic.ListView):
    model = ShoppingItem
    context_object_name = 'shopping_items'

    def get_queryset(self):
        return ShoppingItem.objects.filter(is_completed=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_items'] = ShoppingItem.objects.filter(is_completed=True)
        return context


class EditShoppingItem(generic.UpdateView):
    model = ShoppingItem
    context_object_name = 'shopping_item'
    fields = '__all__'
    success_url = '/'


class DeleteShoppingItem(generic.DeleteView):
    model = ShoppingItem
    success_url = '/'
