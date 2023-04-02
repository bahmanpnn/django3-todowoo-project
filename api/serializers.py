from rest_framework import serializers
from todo.models import Todo


class TodoCompletedListSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        exclude = ("user",)
