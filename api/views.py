from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo

from .serializers import TodoCompletedListSerializer


class TodoCompletedListView(generics.ListAPIView):
    serializer_class = TodoCompletedListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
