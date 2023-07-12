import json
import os
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.channel_id = channel_id
        self.title = channel['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.count_subscribers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"{self.title}, {self.url}"

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return self.count_subscribers + other.subscriber_count

    def __sub__(self, other):
        return self.count_subscribers - other.subscriber_count

    def __gt__(self, other):
        return self.count_subscribers > other.subscriber_count

    def __ge__(self, other):
        return self.count_subscribers >= other.subscriber_count

    def __lt__(self, other):
        return self.count_subscribers < other.subscriber_count

    def __le__(self, other):
        return self.count_subscribers <= other.subscriber_count



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""


        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> build:
        """Возвращающий объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.API_KEY)

    def to_json(self, filename) -> None:
        """Функция сохраняющая в файл значения атрибутов класса"""
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=2)
