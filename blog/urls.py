from django.urls import path
from . import views

# path(route, view, kwargs=None, name=None)
# routeに対するview,routeに対するname
# 簡単に言えば、アクセスするアドレス、呼び出す処理、パス名
# このフォルダまでのパスはすでについているので、それ以降を記載する。
# ''ということは、http://127.0.0.1:8000/ ということになる。つまりこのアプリが呼ばれたとき最初に開かれる画面。

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('chat/', views.chat, name='chat'),
    path('ajax-number/', views.ajax_number, name='ajax_number'),
    path('ajax_chatReg/', views.ajax_chatReg, name='ajax_chatReg'),
    
    
]