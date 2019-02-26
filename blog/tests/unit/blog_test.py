from blog import Blog
from post import Post
from unittest import TestCase


class BlogTest(TestCase):
    def test_blog(self):
        blog = Blog("Test blog", "Sergiy Mushtyn")
        self.assertEqual(blog.title, "Test blog")
        self.assertEqual(blog.author, "Sergiy Mushtyn")
        self.assertListEqual(blog.posts, [])

    def test_repr_no_posts(self):
        blog = Blog("Test blog", "Sergiy Mushtyn")
        self.assertEqual("Test blog by Sergiy Mushtyn: 0 posts", str(blog))

    def test_repr_1_post(self):
        blog = Blog("Test blog", "Sergiy Mushtyn")
        blog.create_post("Test post", "This is a test post content")
        self.assertEqual("Test blog by Sergiy Mushtyn: 1 post", str(blog))

    def test_create_post(self):
        blog = Blog("Test blog", "Sergiy Mushtyn")
        blog.create_post("Test post", "This is a test post content")
        self.assertEqual(str(blog.posts[0]), "Test post: This is a test post content")
        self.assertTrue(len(blog.posts) == 1)

    def test_blogs_json(self):
        blog = Blog("Test blog", "Sergiy Mushtyn")
        blog.create_post("Test post", "This is a test post content")
        self.assertEqual(blog.json(),
                         {"title": "Test blog",
                          "author": "Sergiy Mushtyn",
                          "posts": [
                              {
                              "title": "Test post",
                              "content": "This is a test post content"
                          }]
                          })
