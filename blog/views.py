from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Chat
from .forms import PostForm,ChatForm
from django.http import JsonResponse

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
    
    form = ChatForm()
    return render(request, 'blog/chat.html', {'form': form})

# chat画面の非同期通信用
def ajax_number(request):
    if request.POST.get('number1') is None:
        number1 = 0
    else:
        number1 = int(request.POST.get('number1'))
    if request.POST.get('number2') is None:
        number2 = 0
    else:
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
    title = request.POST.get('title')
    text = request.POST.get('text')
    #リクエストがPOSTの場合
    if request.method == 'POST':
        sample = Chat(author=request.user,title=title, text=text,published_date = timezone.now())
        sample.save()       
        
    d = {
        'text': text,
    }
    return JsonResponse(d)
