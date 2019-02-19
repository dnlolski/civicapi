from rest_framework import generics
from .models import Vote
from .serializers import VoteSerializer 


class VotesList(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
