from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ("author", "title", "text")

        widgets = { # the first key is going to respond to a field
            # key:forms.widgets actual area
            # so title(form model) is applied to textInput widget in django.forms
            "title":forms.TextInput(attrs={'class':"textinputclass"}), # sub dictionary, it's connected to our css class.
            "text":forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"}),
            # editable medium-editor-textarea is made by mediam then we are going to import and apply to it

        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
# widgets is inside meta
        widgets = {
            "author":forms.TextInput(attrs={"class":"textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"}),
        }
