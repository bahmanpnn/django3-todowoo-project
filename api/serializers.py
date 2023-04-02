from rest_framework import serializers
from todo.models import Todo


class TodoCompletedListSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        exclude = ("user",)


class TodoAddToCompleteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id',)
        read_only_fields = ("title", "memo", "created", "datecompleted", "important")
