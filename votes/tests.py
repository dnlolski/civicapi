from django.test import TestCase
from django.utils import timezone
from .serializers import VoteSerializer
from .models import Vote
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

        self.assertEqual(set(data.keys()), set(['subject', 'vote_taken', 'ayes', 'nays']))


    def test_vote_taken_content(self):
        data = self.serializer.data

        self.assertEqual(data['vote_taken'], self.vote_attributes['vote_taken'])
    

    def test_nays_lower_bound(self):
        self.serializer_data['nays'] = timezone.now()

        serializer = VoteSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['nays']))
