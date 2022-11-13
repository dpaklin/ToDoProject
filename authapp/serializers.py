from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import TodoUser


class TodoUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        fields = ('username', 'first_name', 'last_name', 'email',)
