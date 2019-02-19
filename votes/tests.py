from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory
from .serializers import VoteSerializer
from .models import Vote
from .views import VotesList
import requests
import unittest


class TestVoteSerializer(unittest.TestCase):

    def setUp(self):
        self.vote_attributes = {
            'subject': 'TestDjango',
            'vote_taken': timezone.now().isoformat(),
            'ayes': int('10'),
            'nays': int('55')
        }

        self.serializer_data = {
            'subject': 'Test123',
            'vote_taken': timezone.now(),
            'ayes': 5,
            'nays': 60
        }

        self.vote = Vote.objects.create(**self.vote_attributes)
        self.serializer = VoteSerializer(instance=self.vote)


    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'subject', 'vote_taken', 'ayes', 'nays']))


    def test_vote_taken_content(self):
        data = self.serializer.data

        self.assertEqual(data['vote_taken'], self.vote_attributes['vote_taken'])
    

    def test_nays_lower_bound(self):
        self.serializer_data['nays'] = timezone.now()

        serializer = VoteSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['nays']))


class TestVoteCreateApi(unittest.TestCase):

    def setUp(self):
        self.vote_attributes = {
            'subject': 'TestDjango',
            'vote_taken': timezone.now().isoformat(),
            'ayes': int('10'),
            'nays': int('55')
        }

        self.vote_post_attributes = {
            'subject': 'PostMethod',
            'vote_taken': timezone.now().isoformat(),
            'ayes': int('23'),
            'nays': int('12')
        }

        self.vote = Vote.objects.create(**self.vote_attributes)
        self.view = VotesList.as_view()
        self.factory = APIRequestFactory()
        # self.serializer = VoteSerializer(instance=self.vote)

    
    def test_get_method(self):
        request = self.factory.get('votes/')
        response = self.view(request)

        self.assertEqual(response.status_code, 200)


    def test_post_method(self):
        request = self.factory.post('votes/', self.vote_post_attributes, format='json')
        response = self.view(request)
        
        self.assertEqual(response.status_code, 201)

