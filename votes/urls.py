from django.conf.urls import url
from .views import VotesList



urlpatterns = [
    url('', VotesList.as_view()),
]