from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('issues', views.IssueViewSet, basename='issue')
router.register('developers', views.DeveloperViewSet, basename='developer')

developer_issue = routers.NestedDefaultRouter(
    router, 'developers', lookup='developer')

developer_issue.register(
    'assign-issue', views.DeveloperAssignIssueViewSet,
    basename='developer-issue')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(developer_issue.urls))
]
