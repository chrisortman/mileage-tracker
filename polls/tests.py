from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question
# Create your tests here.

class Player(object):
    pass

class SparringRoom(object):
    def enter(self, player):
        
        if player.rope:
            return {'message' : 'You have a rope!'}
        else:
            return {'message' : 'No rope for you'}

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=20)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
        
    def test_message_user_with_rope(self):
        player = Player()
        player.rope = True
        room = SparringRoom()
        output = room.enter(player)
        self.assertEqual(output['message'], "You have a rope!")
        
    def test_message_user_with_rope(self):
        player = Player()
        player.rope = False
        room = SparringRoom()
        output = room.enter(player)
        self.assertEqual(output['message'], "No rope for you")