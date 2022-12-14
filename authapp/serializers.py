from rest_framework.serializers import ModelSerializer
from .models import TodoUser


class TodoUserSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email',)
