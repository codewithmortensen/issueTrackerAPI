
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import serializers, models


ALLOWED_HTTP_METHOD = ['get', 'post', 'patch', 'delete', 'head', 'options']


class IssueViewSet(ModelViewSet):
    http_method_names = ALLOWED_HTTP_METHOD
    queryset = models.Issue.objects.select_related(
        'user').select_related('assign_to__user').all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return serializers.UpdateIssueSerializer
        if self.request.method == 'POST':
            return serializers.CreateIssueSerializer
        return serializers.IssueSerializer


class DeveloperViewSet(ModelViewSet):
    http_method_names = ALLOWED_HTTP_METHOD
    queryset = models.Developer.objects.select_related('user').all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return serializers.UpdateDeveloperSerializer
        if self.request.method == 'POST':
            return serializers.CreateDeveloperSerializer
        return serializers.DeveloperSerializer


class DeveloperAssignIssueViewSet(GenericViewSet, ListModelMixin):
    def get_queryset(self):
        return models.Issue.objects.select_related('user').select_related('assign_to__user').filter(assign_to_id=self.kwargs['developer_pk'])
    serializer_class = serializers.IssueSerializer
