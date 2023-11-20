from rest_framework import serializers
from . import models
from core.models import User


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        # to be replace with the default auth user model
        model = User
        fields = ['first_name', 'last_name', 'email']


class SimpleDeveloperSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = models.Developer
        fields = ['user']


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


class DeveloperSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    user_id = serializers.IntegerField()

    def validate_user_id(self, user_id):
        if models.Developer.objects.filter(pk=user_id).exists():
            raise serializers.ValidationError(
                'A developer with this user ID already exist')
        return user_id

    class Meta:
        model = models.Developer
        fields = [
            'id', 'user', 'user_id', 'status',
            'birth_date', 'gender', 'phone'
        ]

    def create(self, validated_data):

        return super().create(validated_data)


class UpdateDeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Developer
        fields = ['status', 'birth_date', 'gender', 'phone']
