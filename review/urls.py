from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('reviews', views.getReview),
    path('review/create', views.createReview),
    path('review/update/<str:pk>', views.updateReview),
    path('review/delete/<str:pk>', views.deleteReview),

    # path('google/login',GoogleView),

]
