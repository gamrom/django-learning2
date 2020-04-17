from django.urls import path
from .views import *

app_name = "posts"
urlpatterns = [
    path('new/', new , name="new"),
    path('create/', create, name="create"),
]
