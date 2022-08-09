from django.contrib import admin
from .models import Post    #「.」はカレントディレクトリ　同じフォルダ内にあるmodelsファイルからimport

admin.site.register(Post)