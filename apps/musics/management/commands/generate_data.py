# Python modules
from typing import Any, Optional
import datetime
import random
# Django modules
from django.core.management.base import BaseCommand
# Third part modules
import requests
from requests import Response
from bs4 import BeautifulSoup
import names
# Project modules
from musics.models import Author, Music, Genre
from auths.models import MyUser


class Command(BaseCommand):
    """ Custom command for generate data """
    def __init__(self, *args, **kwargs) -> None:
        self.email_patterns = [
            '@gmail.com',
            '@mail.ru',
            '@bk.ru',
            '@yahoo.com',
            '@inbox.ru'
        ]
        self.genres = [
            'Pop',
            'Rok',
            'Rap',
            'Hiphop',
            'Rythm and blues',
            'Country',
            'Funk',
            'Folk',
            'Jazz',
            'Disco',
            'Classical'
        ]
    
    def generate_genre(self) -> None:
        
        for g in self.genres:
            if Genre.objects.filter(title=g).count() == 0:
                Genre.objects.create(
                    title=g
                )

    def generate_music(self) -> None:
        emails: list = []
        for i in MyUser.objects.all():
            emails.append(i.email)

        url: str = 'https://sefon.pro/top/'
        headers: dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result: Response = requests.get(url, headers=headers)
        soup = BeautifulSoup(result.text)
        tags = soup.find_all(class_="mp3")
        for t in tags:
            artist_tag = t.find(class_="artist_name")
            song_tag = t.find(class_="song_name")
            duration_tag = str(t.find("span", class_="value"))

            user: MyUser =  MyUser.objects.filter(first_name=artist_tag.text).first()

            if not user:
                email = names.get_first_name() + self.email_patterns[random.randrange(0, len(self.email_patterns))]
                while email in emails:
                    email = names.get_first_name() + self.email_patterns[random.randrange(0, len(self.email_patterns))]

                emails.append(email)

                user = MyUser.objects.create(
                    email=email,
                    first_name=artist_tag.text,
                    is_active=True
                )
            else:
                user.first_name = artist_tag.text
                user.save()
            
            author: Author = Author.objects.filter(user=user).first()

            if not author:
                author = Author.objects.create(
                    user=user
                )
            
            genre = Genre.objects.get(title=self.genres[random.randrange(0, len(self.genres))])

            duration: datetime.time = None
            try:
                duration = datetime.time(hour=int(duration_tag[20:22]), minute=int(duration_tag[23:25]))
            except ValueError as e:
                duration = datetime.datetime.now()
            
            music: Music = Music.objects.filter(title=song_tag.text).first()

            if not music:
                music = Music.objects.create(
                    status='BR',
                    title=song_tag.text,
                    duration=duration,
                    author=author,
                )
                music.genre.set((genre, ))
                music.save()

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """ Handle data filling """
        start: datetime = datetime.datetime.now()

        self.generate_genre()
        self.generate_music()

        end: datetime = datetime.datetime.now()

        print(
            f'Generated in: {(end - start).total_seconds()} seconds'
        )