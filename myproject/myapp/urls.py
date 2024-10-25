from django.urls import path
from .views import signup, profile, item_list, item_create, item_update, item_delete

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('items/', item_list, name='item_list'),
    path('items/create/', item_create, name='item_create'),
    path('items/update/<int:pk>/', item_update, name='item_update'),
    path('items/delete/<int:pk>/', item_delete, name='item_delete'),
]
