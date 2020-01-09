from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippets-detail'),
    path('', views.SnippetList.as_view(), name='snippets-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
