import django_tables2 as tables
from githubApi.models import UserDetail


class UserTable(tables.Table):
    class Meta:
        model = UserDetail
        template_name = 'django_tables2/semantic.html'