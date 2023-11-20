from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('issues', views.IssueViewSet, basename='issue')
urlpatterns = [
    path('', include(router.urls))
]
