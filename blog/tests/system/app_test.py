from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    """
    To cover the function that printing smth out by the unit test the 'unittest.mock.patch' is used.
    The 'print' func is patched and so that it is checking that the print func has been called with <some_value>
    """

    def test_print_blogs(self):
        blog = Blog("Test", "Sergiy Mushtyn")
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Sergiy Mushtyn: 0 posts")
