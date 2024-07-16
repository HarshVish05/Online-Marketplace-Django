from django.urls import path

from item.views import detail, add_new, delete_item, edit_item, items


"""Adding app_name = 'item' in your urls.py file within a Django application is used to specify 
a namespace for your app's URL patterns. This can be very useful when you have multiple apps 
with URL patterns that might have the same names. By defining an app_name, you can avoid 
naming conflicts and make your URL references more explicit and organized."""

app_name = 'item'

urlpatterns = [
    path('', items, name= 'items' ),
    path('<int:pk>/', detail, name= 'detail'),  # pk has to be same as we have used in detail view
    path('additem/', add_new, name= "additem" ),
    path('<int:pk>/delete/', delete_item, name= 'deleteItem'),
    path('<int:pk>/edit/', edit_item, name= 'editItem'),
]
