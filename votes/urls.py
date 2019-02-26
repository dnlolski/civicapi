from django.urls import path
from .views import VotesList, VoteDetail


urlpatterns = [
    path('', VotesList.as_view()),
    path('<int:pk>', VoteDetail.as_view()),
]