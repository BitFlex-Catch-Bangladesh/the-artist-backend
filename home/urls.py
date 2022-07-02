from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('home/banners', views.getHomeBanner),
    path('home/banner/add', views.addHomeBanner),

    # path('google/login',GoogleView),

]
