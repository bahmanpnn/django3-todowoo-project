from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed', views.TodoCompletedListView.as_view(), name="todo-completed-list")
]
