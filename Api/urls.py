from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, GroupViewSet, snippet_detail, snippet_list, \
    SnippetList, SnippetDetail, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

onlyapi = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('users1/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(onlyapi)


urlpatterns = [
                  path('', include(router.urls)),
                  path('/api-auth', include('rest_framework.urls', namespace='rest_framework'))
              ] + urlpatterns
