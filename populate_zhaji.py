import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_zhaji_project.settings')

import django
django.setup()

from zhaji.models import Category, Book


def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        name="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        name="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        name="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        name="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        name="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        name="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        name="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        name="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Book.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, name, url, views=0):
    p = Book.objects.get_or_create(category=cat, name=name)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Zhaji population script..."
    populate()
