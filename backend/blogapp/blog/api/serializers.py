from rest_framework import serializers
from blog.models import Blog, Category, Tag, Yorum, Profile

class TagSerializer(serializers.ModelField):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

        
class YorumSerializer(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Yorum
        # fields = '__all__'
        exclude = ['blog']  


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    yorumlar = YorumSerializer(read_only=True, many=True)
    blog_sahibi = ProfileSerializer(read_only=True)
    image = serializers.ImageField()


    # blog_sahibi = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['user', 'text',]

    

