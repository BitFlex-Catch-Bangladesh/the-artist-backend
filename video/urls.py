from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('videos', views.getVideo),
    path('video/create', views.createVideo),
    path('video/update/<str:pk>', views.updateVideo),
    path('video/delete/<str:pk>', views.deleteVideo),

    # path('google/login',GoogleView),

]
