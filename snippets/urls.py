from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippets-detail'),
    path('', views.api_root, name='snippets-root'),
    path('<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
