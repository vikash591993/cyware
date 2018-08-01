from django.conf.urls import url
import githubApi
from githubApi.views import Home
from githubApi.views import GithubLogin
from django.contrib.auth.views import login
from githubApi.views import GeneratePDF

urlpatterns = [
    url(r'^$', GithubLogin, name='GithubLogin'),
    url(r'^showdetail/$', Home, name='showdetail'),
    url(r'^generateReport/$', GeneratePDF , name='generateReport'),
]
