# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import re_path, include
from todo_api import urls as todo_urls

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path('todos/', include(todo_urls)),
]