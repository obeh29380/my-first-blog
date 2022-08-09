from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # author は現在ログインしている人,
        # created_date は（コードによって）自動的に記事を書いた日時が設定されます。