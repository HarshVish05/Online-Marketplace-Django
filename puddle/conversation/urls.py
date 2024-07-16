from django.urls import path


from .views import new_conversation, inbox, detail_msg

app_name = "conversation"

urlpatterns = [
    path('new/<int:item_pk>/', new_conversation, name= "new_conversation"),
    path('', inbox, name= 'inbox'),
    path('<int:pk>/', detail_msg, name="detail_msg")
]
