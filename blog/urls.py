from django.urls import path
from rest_framework import routers

from .api.views import ListPosts, ScorePostViewSet

router = routers.SimpleRouter()
router.register(r"posts", ListPosts)
router.register(r"posts", ScorePostViewSet)

urlpatterns = [
    *router.urls,
]
