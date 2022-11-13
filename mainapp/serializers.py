from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField, ModelSerializer
from .models import Project, ToDo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    todo = HyperlinkedRelatedField(read_only=True, many=True, view_name='todo-detail')

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    # project = HyperlinkedRelatedField(read_only=True, view_name='project-detail')
    # creator = HyperlinkedRelatedField(read_only=True, view_name='todouser-detail')

    class Meta:
        model = ToDo
        fields = '__all__'
