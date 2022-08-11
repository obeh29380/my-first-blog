"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# include について
# blog.urls は　blogアプリケーションのurlsファイルを示す。
# 難しいので、アプリ名.urls という形でDjangoで決まっていると思っておくのが良い。内部的に名前解決しているんだろう。
# 本アプリの場合は、blogとmysiteでアプリが分かれているという扱い？
# Djangoが自動で作成する管理画面=プロジェクト管理フォルダ(mysite)、ブログの編集やら＝アプリ管理フォルダ（blog)
# こうやってアプリ毎に分けることで、何個もアプリを追加した場合、その時作成しているアプリのフォルダのみ見ればOKになる
# →いちいちmysiteフォルダのurl.pyを直すより、作成中のアプリのフォルダ内のurl直す方が分かりやすいし、管理しやすい 
# そもそも、「アプリケーションのアドレスは対象アプリケーションフォルダ内で管理する」という基本原則がある。


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]