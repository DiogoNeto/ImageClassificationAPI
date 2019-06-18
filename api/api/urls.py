from django.contrib import admin
from django.urls import path, include
from core.views import ImageViewSet
from rest_framework import routers 
from core import views

router = routers.DefaultRouter()
router.register(r'images',ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('faces/', views.nFaces),
    #path('xpto/', views.xpto),
    # path('landmarks', views.face_recognition),

    path('api-auth', include('rest_framework.urls')),

    
]
