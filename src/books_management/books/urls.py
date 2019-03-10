from django.conf.urls import url, include
from django.contrib import admin
from .views import BooksViewSet, UserProfileViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework import routers

# router = routers.SimpleRouter(trailing_slash= False)
# class OptionalSlashRouter(SimpleRouter):
#     def __init__(self):
#         self.trailing_slash = '/?'
#         super(SimpleRouter, self).__init__()
# router.register('book',BooksViewSet)
# router.register('profile', UserProfileViewSet)

class OptionalTrailingSlashRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(OptionalTrailingSlashRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'

router = OptionalTrailingSlashRouter()
router.register('book',BooksViewSet)

urlpatterns = [
    url(r'^',include(router.urls))
]
