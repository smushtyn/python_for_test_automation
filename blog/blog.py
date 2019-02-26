from post import Post


class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return "{} by {}: {} post{}".format(self.title,
                                            self.author,
                                            len(self.posts),
                                            's' if len(self.posts) != 1 else '')

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }


# test_blog = Blog("First own blog", "Sergiy Mushtyn")
# print(test_blog)
# test_blog.create_post("Beautiful life", "Such a beautiful life")
# test_blog.create_post("Beauasacacsascacasctiful life", "Such a beascacacs;lautiful life")
#
# print(test_blog)
# print(test_blog.json())
