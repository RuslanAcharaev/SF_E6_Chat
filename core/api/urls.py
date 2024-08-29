from django.urls import include, path, re_path
from rest_framework import routers

from .views import ProfileViewSet, RoomViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
