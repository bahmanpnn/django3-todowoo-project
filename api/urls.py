from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreateView.as_view(), name="todo-list"),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyView.as_view(), name="todo-detail-page"),
    path('todos/<int:pk>/complete', views.TodoCompleteView.as_view(), name="todo-update-to-complete-detail-page"),
    path('todos/completed', views.TodoCompletedListView.as_view(), name="todo-completed-list"),

    # authentication
    path('signup/', views.signup, name="signup-user"),

]
