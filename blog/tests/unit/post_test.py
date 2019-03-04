from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def create_post(self):
        return Post("Test title", "This is my first post")

    def test_create_post(self):
        self.assertEqual(self.create_post().title, "Test title")
        self.assertEqual(self.create_post().content, "This is my first post")

    def test_repr(self):
        self.assertEqual(str(self.create_post()), 'Test title: This is my first post')

    def test_json(self):
        self.assertEqual(self.create_post().json(), {'title': "Test title", 'content': 'This is my first post'})
