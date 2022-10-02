from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Post
from .serializers import ListPostSerializer, PostScoreSerializer


class ListPosts(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.annotate(
        score_average=F('score_sum') / F('score_count'),
    )
    serializer_class = ListPostSerializer


class ScorePostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostScoreSerializer

    @action(detail=True, methods=["POST"])
    def score(self, request, pk=None):
        post = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

