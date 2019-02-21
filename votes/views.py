from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer
from .models import Vote
from .serializers import VoteSerializer 


class VotesList(generics.ListCreateAPIView):
    renderer_classes = (
        JSONRenderer, 
        TemplateHTMLRenderer, 
        BrowsableAPIRenderer,
        )
    template_name = "vote_list.html"
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
