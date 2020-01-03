from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    path('', views.snippet_list, name='snippets-list'),
    path('list/', views.snippet_list, name='snippets-list'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippets-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
