# todo/api/urls.py : API urls.py
#rom django.conf.urls import url
from django.urls import re_path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    re_path('api', TodoListApiView.as_view()),
    re_path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]