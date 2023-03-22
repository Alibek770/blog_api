from rest_framework import generics, permissions

from comment import serializer
from post.permissions import ISAuthorOrAdminOrPostOwner
from .models import Comment

class CommentCreateView(generics.CreateAPIView):
    # queryset = Comment.objects.all()
    serializer_class = serializer.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializers_class = serializer.CommentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return ISAuthorOrAdminOrPostOwner(),
        return permissions.AllowAny(),



