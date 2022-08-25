from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Chat
from .forms import PostForm,ChatForm
from .listen import start_listen
from django.http import JsonResponse,HttpResponse
import logging

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
    else:
        form = PostForm()
        
    if form.is_valid():
        post = form.save(commit=False)   #authorを追加するため、コミットはしない
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# chat画面を開く用
def chat(request):
    # 全件取得
    queryset = Chat.objects.all()
    
    text=""
    
    for idata in queryset:
        text += idata.text + "\n"
    
    data = {'title':'hello',
            'text':text}
        
    form = ChatForm(
        data
    )
    
    # start_listen(1)
    
    return render(request, 'blog/chat.html', {'chatform': form})

# chat画面の非同期通信用
def ajax_number(request):
    number1 = int(request.POST.get('number1'))
    number2 = int(request.POST.get('number2'))
    plus = number1 + number2
    minus = number1 - number2
    d = {
        'plus': plus,
        'minus': minus,
    }
    return JsonResponse(d)

# chat画面の非同期通信用

def ajax_chatReg(request):
    #リクエストがPOSTの場合
    authorid = int(request.POST.get('authorid'))
    Ptitle = request.POST.get('title')
    Ptext = request.POST.get('text')
    
    # sample = Chat(author = Pauthor,title = Ptitle,text = Ptext,published_date = timezone.now())
    # author_idは、値を指定するなら、int型で、Djangoが自動で作成するユーザテーブル(user_auth)に存在するidでなければエラーになる。
    # リクエストユーザーのインスタンスを渡してやれば、その中からIDを拾って登録してくれる。
    obj = Chat(author_id=1,title=Ptitle,text=Ptext,published_date=timezone.now())
    obj.save()       
    
    
    
    # if request.method == "POST":
    #     form = ChatForm(request.POST)
        
    # else:
    #     form = ChatForm()
        
    # if form.is_valid():
    #     post = form.save(commit=False)   #authorを追加するため、コミットはしない
    #     post.author = request.user
    #     post.published_date = timezone.now()
    #     post.save()
        
        
    d = {
        'text': Ptext,
    }
    return JsonResponse(d)
