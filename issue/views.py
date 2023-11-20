from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS
from . import serializers, models


@api_view()
def issue(request):
    return Response('ok')


ALLOWED_HTTP_METHOD = ['get', 'post', 'patch', 'delete', 'head', 'options']


class IssueViewSet(ModelViewSet):
    http_method_names = ALLOWED_HTTP_METHOD
    queryset = models.Issue.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return serializers.UpdateIssueSerializer
        if self.request.method == 'POST':
            return serializers.CreateIssueSerializer
        return serializers.IssueSerializer


class DeveloperViewSet(ModelViewSet):
    http_method_names = ALLOWED_HTTP_METHOD
    queryset = models.Developer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return serializers.UpdateDeveloperSerializer
        return serializers.DeveloperSerializer


class DeveloperAssignIssueViewSet(ModelViewSet):
    # http_method_names = SAFE_METHODS

    def get_queryset(self):
        return models.Issue.objects.filter(assign_to_id=self.kwargs['developer_pk'])
    serializer_class = serializers.IssueSerializer
