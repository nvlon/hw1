from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .models import Review
from .models import Director
from .serializers import MovieSerializer
from .serializers import ReviewSerializer
from .serializers import DirectorSerializer


@api_view(['GET'])
def reviews(request):
    review_list = Review.objects.all()
    review_json =ReviewSerializer(instance=review_list, many=True).data
    return Response(data=review_json)


@api_view(['GET'])
def reviews_detail(request,id ):
    try:
     review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    review_json = ReviewSerializer(instance=review_detail).data
    return Response(data=review_json)


@api_view(['GET'])
def directors(request):
    director_list = Director.objects.all()
    director_json = DirectorSerializer(instance=director_list, many=True).data
    return Response(data=director_json)


@api_view(['GET'])
def directors_detail(request,id ):
    try:
     director_detail = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    director_json = DirectorSerializer(instance=director_detail).data
    return Response(data=director_json)


@api_view(['GET'])
def movies(request):
    """ List of objects = QuerySet """
    movie_list = Movie.objects.all()

    """Reformat (Serialize) list of objects to JSON"""
    movie_json = MovieSerializer(instance=movie_list, many=True).data

    """Return dict objects by JSON file"""
    return Response(data=movie_json)



@api_view(['GET'])
def movies_detail(request, id):
    try:
      movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    data= MovieSerializer(movie_detail).data

    return Response(data=data)


@api_view(['GET'])
def director(request):
    """Logic"""
    data_dict = {
        'text': 'Hello World',
        'int': 1000,
        'float': 2.5,
        'bool':True,
        'list':[1,2,3],
        'dict':{'key', 'value'}
    }
    return Response(data=data_dict, status=status.HTTP_226_IM_USED)

