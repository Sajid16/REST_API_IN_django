from rest_framework import serializers
from Blog.models import Category, Articles

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class articlesSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField(source='get_category_name')
    # category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Articles
        fields = ['id','name', 'description', 'category_name', 'created_at', 'updated_at']

    # getting field name from foreign key instead of id
    def get_category_name(self, obj):
        return obj.category.name
