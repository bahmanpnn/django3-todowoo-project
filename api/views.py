from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo
from .serializers import TodoCompletedListSerializer, TodoAddToCompleteListSerializer
from django.utils import timezone


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoCompletedListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoCompletedListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoCompleteView(generics.UpdateAPIView):
    serializer_class = TodoAddToCompleteListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()


class TodoCompletedListView(generics.ListAPIView):
    serializer_class = TodoCompletedListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
