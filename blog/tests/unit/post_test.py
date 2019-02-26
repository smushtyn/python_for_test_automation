from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        test_post = Post("Test title", "This is my first post")
        self.assertEqual(test_post.title, "Test title")
        self.assertEqual(test_post.content, "This is my first post")

    def test_repr(self):
        test_post = Post("Test title", "This is my first post")
        self.assertEqual(str(test_post), 'Test title: This is my first post')

    def test_json(self):
        test_post = Post("Test title", "This is my first post")
        self.assertEqual(test_post.json(), {'title': "Test title", 'content': 'This is my first post'})
