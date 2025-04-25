from django.contrib import admin
from django.urls import re_path
from student.views import view_hello, view_record, view_hello_20

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^hello1/', view_hello, name='home'),
    re_path(r'^hello20/', view_hello_20),
    re_path(r'', view_record),
]
