from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
     path('', include(router.urls))
]

# urlpatterns = [
#     path('',
#          views.api_root,
#          name='snippet-root'),
#     path('api-auth/',
#          include('rest_framework.urls')),
#     path('<int:pk>/',
#          views.SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/',
#          views.SnippetList.as_view(),
#          name='snippet-list'),
#     path('<int:pk>/highlight/',
#          views.SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail'),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
