from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Article 
        fields = "__all__"





"""
# Using serializers.Serializer
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(read_only=True)
    published = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Article.object.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance
"""