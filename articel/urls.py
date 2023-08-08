from django.urls import path, include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('articel', views.ArticelApi)
router.register('category', views.CateGoryApi)
router.register('user', views.UserApi)

urlpatterns = [
    path('', include(router.urls)),  
]
