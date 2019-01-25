from django.conf.urls import url
from api.views import course, news, login

urlpatterns = [
    url(r'^(?P<version>[v1|2]+)/course/$', course.CourseView.as_view({"get": "list"})),
    url(r'^(?P<version>[v1|2]+)/course/(?P<pk>\d+)/$', course.CourseView.as_view({"get": "retrieve"})),

    url(r'^(?P<version>[v1|2]+)/news/$', news.NewsView.as_view({"get": "list"})),
    url(r'^(?P<version>[v1|2]+)/news/(?P<pk>\d+)/$', news.NewsView.as_view({"get": "retrieve"})),

    url(r'^(?P<version>[v1|2]+)/login/$', login.LoginView.as_view()),

    url(r'^(?P<version>[v1|2]+)/collect/$', news.CollectView.as_view()),
    url(r'^(?P<version>[v1|2]+)/agree/$', news.AgreeView.as_view()),
    url(r'^(?P<version>[v1|2]+)/comment/$', news.CommentView.as_view()),
]
