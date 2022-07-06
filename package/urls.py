from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('packages', views.getPackages),
    path('packages/<str:pk>', views.getPackagesByCategory),
    path('package/create', views.createPackage),
    path('package/update/<str:pk>', views.updatePackage),
    path('package/delete/<str:pk>', views.deletePackage),

    # path('google/login',GoogleView),

]
