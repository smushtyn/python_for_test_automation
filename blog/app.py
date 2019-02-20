blogs = dict()


def menu():
    #  Shows the available blogs for the user;
    #  Let the user to make some choice
    #  Do smth with that choice
    #  Eventually exit
    print_blogs()


def print_blogs():
    for _, blog in blogs.items():
        print("- {}".format(blog))

