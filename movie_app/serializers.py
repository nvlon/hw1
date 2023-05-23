from rest_framework import serializers
from .models import Movie
from .models import Director
from .models import Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ' id title'.split()
        # exclude = 'description'.split()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id title'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ' id description'.split()


