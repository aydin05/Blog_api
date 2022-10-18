from rest_framework import serializers

from myapp.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'created_at', 'update_at', ]


class BlogPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(write_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'update_at', 'image', 'category', ]

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get_or_create(**category_data)
        validated_data['category'] = category[0]
        return super().create(validated_data)
