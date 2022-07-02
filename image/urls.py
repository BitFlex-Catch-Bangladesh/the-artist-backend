from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('images', views.getImage),
    path('image/add', views.addImage),
    path('image/delete/<str:pk>', views.deleteImage),

    # path('google/login',GoogleView),

]
