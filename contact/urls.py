from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('contacts', views.getContact),
    path('contact/create', views.createContact),
    path('contact/delete/<str:pk>', views.deleteContact),

    # path('google/login',GoogleView),

]
