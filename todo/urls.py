from django.urls import path
from todo import views

urlpatterns = [
    path('', views.ShoppingItems.as_view(), name='shopping-items'),
    path('create/', views.CreateShoppingItem.as_view(), name='create-shopping-item'),
    path('<int:pk>/edit/', views.EditShoppingItem.as_view(), name='edit-shopping-item'),
    path('<int:pk>/delete/', views.DeleteShoppingItem.as_view(), name='delete-shopping-item')
]
