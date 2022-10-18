from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.api.serializers import BlogPostSerializer
from myapp.models import Post, Category


class BlogAPIView(APIView):
    serializer_class = BlogPostSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get_queryset():
        post = Post.objects.all()
        return post

    def get(self, request, *args, **kwargs):
        post = self.get_queryset()
        serializer = BlogPostSerializer(post, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

# class CategoryAPIView(APIView):
#     serializer_class = CategorySerializer
#
#     @staticmethod
#     def get_queryset():
#         category = Category.objects.all()
#         return category
#
#     def get(self, request, *args, **kwargs):
#         category = self.get_queryset()
#         serializer = CategorySerializer(category, many=True)
#
#         return Response(serializer.data)
