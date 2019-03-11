from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from . import serializers
from . import models


"""def home_view(request):
    output = " <html> <em> Book Management </em> </html> "
    return HttpResponse(output)
"""

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.BookStoreSerializer
    queryset = models.BookStore.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author','isbn','publication',)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

        # authentication_classes = (TokenAuthentication,)
        # permission_classes = (permissions.UpdateOwnProfile,)

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'email',)




