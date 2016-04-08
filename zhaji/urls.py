from django.conf.urls import url
from zhaji import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^book/(?P<book_isbn>[\d]+)/$', views.book, name='book'),
        url(r'^note/(?P<note_pk>[\d]+)/$', views.note, name='note'),
        #url(r'^add_category/$', views.add_category, name='add_category'),
        #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
]
