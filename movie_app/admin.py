from django.contrib import admin

from . models import Movie
from .models import Review
from .models import Director


admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Director)