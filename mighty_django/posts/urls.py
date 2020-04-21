from django.urls import path
from .views import *

app_name = "posts"
urlpatterns = [
    path('new/', new , name="new"),
    path('create/', create, name="create"),
    # path('show/', show, name="show"),
    path('show/<int:post_id>/', show, name="show"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update")
]
