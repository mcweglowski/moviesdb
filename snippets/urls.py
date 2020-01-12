from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippets-detail'),
    path('', views.SnippetList.as_view(), name='snippets-list'),
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
