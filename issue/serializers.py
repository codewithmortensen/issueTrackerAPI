from rest_framework import serializers
from . import models
from core.models import User


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        # to be replace with the default auth user model
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class SimpleDeveloperSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = models.Developer
        fields = ['id', 'user']


class IssueSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()
    assign_to = SimpleDeveloperSerializer()

    class Meta:
        model = models.Issue
        fields = [
            'id', 'user', 'title',
            'description', 'status', 'date_created', 'last_update', 'assign_to'
        ]


class UpdateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = ['title', 'description', 'status', 'assign_to']


class CreateIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = ['user', 'title', 'description']
