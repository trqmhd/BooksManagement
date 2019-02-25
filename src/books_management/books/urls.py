from django.conf.urls import url, include
from django.contrib import admin
from .views import BooksViewSet, UserProfileViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('book',BooksViewSet)

# router.register('profile', UserProfileViewSet)


urlpatterns = [

    url (r'',include(router.urls))
]
