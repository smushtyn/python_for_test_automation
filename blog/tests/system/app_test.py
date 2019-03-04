from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    """
    To cover the function that printing smth out by the unit test the 'unittest.mock.patch' is used.
    The 'print' func is patched and so that it is checking that the print func has been called with <some_value>
    """

    def test_menu_calls_print_blogs(self):
        """
        Need to check whether 'print_blogs' func is called from the 'menu' func;
        1. patch 'app.print_blogs' func to check whether it'll be called
        2. As far as whole 'menu()' func will be called -> all instructions inside will be called including 'input'
           which is waiting for the user's input, thus need to be handled to not stuck the test execution
        3. Patch the 'builtins.input' func to replace 'input' with fake input func which will do nothing when
           called -> thus will not cause test execution stucking.
        """
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):  # return_value assigns the value to a call
                app.menu()
                mocked_print_blogs.assert_called()

    def test_mocked_input(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_print_blogs(self):
        blog = Blog("Test", "Sergiy Mushtyn")
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Sergiy Mushtyn: 0 posts")

    def test_create_blog(self):
        """
        side_effect
        If the patched 'input' func is called more than one time - the different args should be passed to it
        patch(return_value=smth) -> will return single value on every patched func call
        This is resolved by 'side_effect' -> the args are listed in that order in which they will be consequently passed
        to the mocked func.
        """
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Blog')

            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_read_blog(self):
        blog = Blog("Test", "Sergiy Mushtyn")
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog("Test", "Sergiy Mushtyn")
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post('Test Post', 'Test Content')
        expected_post = """
--- Test Post ---

Test Content

"""
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_post)
