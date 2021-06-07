from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'hello-viewset', views.HelloViewSet, basename = 'hello-viewset')

# When using the model viewset we don't need to specify the basename
router.register(r'profile', views.UserViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]