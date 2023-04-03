from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo
from .serializers import TodoCompletedListSerializer, TodoAddToCompleteListSerializer
from django.utils import timezone
# signup imports
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.crypto import get_random_string


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            # user = User.objects.create_user(username=data['username'],password=data['password'])
            user.save()
            token = get_random_string(62)
            return JsonResponse({'token': token}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return JsonResponse({'error': "that username has already been taken.please choose another username"},
                                status=status.HTTP_400_BAD_REQUEST)


# --test signup endpoint
# curl -X "POST" http://127.0.0.1:8000/api/signup/ -H 'Content-Type:application/json' \
# -d '{"username":"bahmanpn","password":"12345"}'

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
