from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from . import serializers, models


@api_view()
def issue(request):
    return Response('ok')


class IssueViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return serializers.UpdateIssueSerializer
        if self.request.method == 'POST':
            return serializers.CreateIssueSerializer
        return serializers.IssueSerializer
