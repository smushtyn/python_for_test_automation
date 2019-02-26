class Post(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "{}: {}".format(self.title, self.content)

    def json(self):
        return {
            'title': self.title,
            'content': self.content
        }


# test_post = Post("Test post's title", "This is a test post content")
# print(test_post.json())
