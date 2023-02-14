# Django
from django.test import TestCase

# Local
from .models import (
    Music,
    Author,
    Genre,
)
from auths.models import MyUser

class MusicTestCase(TestCase):
    def setUp(self, title='Test music title'):
        self.user =  MyUser.objects.create_user('test@mail.ru', '12345')
        self.user.first_name = 'Test 1'
        self.user.last_name = 'Test 2'

        self.author = Author.objects.create(
            user=self.user
        )

        self.genre = Genre.objects.create(title='Test Genre')

        self.genres = []

        self.genres.append(Genre.objects.create(title='Genre 1'))
        self.genres.append(Genre.objects.create(title='Genre 2'))
        self.genres.append(Genre.objects.create(title='Genre 3'))

        self.music = Music.objects.create(
            title=title,
            author=self.author,

        )
        
        self.music.genre.set(self.genres)

    def test_genre_creation(self):
        self.assertTrue(isinstance(self.genre, Genre))
        self.assertEqual(self.genre.__str__(), self.genre.title)
    
    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))
        self.assertTrue(isinstance(self.author.user, MyUser))
   
    def test_music_creation(self):
        self.assertTrue(isinstance(self.music, Music))
        self.assertEqual(self.music.__str__(), self.music.title)