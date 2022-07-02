from django.urls import path

from . import views
# from .views import GoogleView

urlpatterns = [
    path('teams', views.getTeams),
    path('team/create', views.createTeam),
    path('team/update/<str:pk>', views.updateTeam),
    path('team/delete/<str:pk>', views.deleteTeam),

    # path('google/login',GoogleView),

]
