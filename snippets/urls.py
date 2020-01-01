from django.urls import path
from . import views


urlpatterns = [
    path('', views.snippet_list, name='snippets-list'),
    path('list/', views.snippet_list, name='snippets-list'),
    path('<int:pk>/', views.snippet_detail, name='snippets-detail'),
]
