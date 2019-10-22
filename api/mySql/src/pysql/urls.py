from django.contrib import admin
from django.urls import path, include
from core.views import ImageViewSet, XPTOViewSet
from rest_framework import routers 
from core import views


router = routers.DefaultRouter()
router.register(r'images',ImageViewSet)
router.register(r'xpto',XPTOViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('faces/<int:id>/', views.nFaces),
    path('xpto/', views.XPTO),
    path('getfaces/<int:id>/',views.geti),
    path('getlandmarks/<int:id>/',views.getl),
    path('geteyes/',views.getEyes),
    path('geteyes2/<int:id>',views.getEyes2),
    path('geteyes3/<int:id>', views.getEyes3),
    path('getsmile/<int:id>', views.getSmile),
    
    path('getsmileurl/<path>/', views.getSmileUrl),
    path('getsmileurl/', views.getSmileUrl),

    path('getsmileurljson/<path>/', views.getSmileUrlJson),
    path('getsmileurljson/', views.getSmileUrlJson),

    path('getsmilejson/<int:id>', views.getSmileJson),
    
    path('profile/<username>/', views.profile),
    path('profile/', views.profile),

    path('getfaceeyes/',views.getFaceEyes),

    #path('landmarks', views.face_recognition),

    path('api-auth', include('rest_framework.urls')),
]
