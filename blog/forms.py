from django import forms

from .models import Post,Chat

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # author は現在ログインしている人,
        # created_date は（コードによって）自動的に記事を書いた日時が設定されます。

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('roomid', 'text',)
        chatline = forms.CharField(label= "チャット内容")
        
        # 追加設定
        widgets = {
            'text': forms.Textarea(attrs={'rows':40, 'cols':50}),
        }
        # author は現在ログインしている人,
        # created_date は（コードによって）自動的に記事を書いた日時が設定されます。
        # ラベルを設定すれば、ラベル名で画面表示、ラベルが無ければIDが表示
