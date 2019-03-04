from blog import Blog
POST_TEMPLATE = """
--- {} ---

{}

"""

MENU_PROMPT ='Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post or "q" to quit: '
blogs = dict()


def menu():
    #  Shows the available blogs for the user;
    #  Let the user to make some choice
    #  Do smth with that choice
    #  Eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for _, blog in blogs.items():
        print("- {}".format(blog))


def ask_create_blog():
    title = input('Enter blog\'s title: ')
    author = input('Enter your name: ')
    blogs[title] = Blog(title, author)


# own implementation of read blog
# def ask_read_blog():
#     blog_to_read = input('Enter the blog\'s title you want to read: ')
#     try:
#         blog = blogs[blog_to_read]
#         print(blog.json())
#     except KeyError:
#         print('No such blog')

def ask_read_blog():
    blog_title = input('Enter the blog title you want to read: ')
    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_to_create_post_in = input('Enter the blog\'s name you want to add post in: ')
    try:
        blog = blogs[blog_to_create_post_in]
        post_title = input('Enter the post\'s title: ')
        post_content = input('Enter the post\'s content: ')
        blog.create_post(post_title, post_content)
    except KeyError:
        print('No such blog')
