from django import forms

from core.models import Tag, Post


# class PostCreate(forms.Form):
#     title = forms.CharField(
#         widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
#     )
#     text = forms.CharField(
#         widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': 20})
#     )
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         required=False,
#         widget=forms.widgets.SelectMultiple(attrs={'class': 'form-control'}),
#         to_field_name='name'
#     )
#     pegi = forms.ChoiceField(choices=Post.PEGI_CHOICES)
#
#     def clean_title(self):
#         if len(self.cleaned_data['title']) < 20:
#             raise forms.ValidationError('Must be more then 20 chars')
#         return self.cleaned_data['title']
#
#     def save(self, user):
#         post = Post.objects.create(
#             title=self.cleaned_data['title'],
#             text=self.cleaned_data['text'],
#             pegi=self.cleaned_data['pegi'],
#             author=user
#         )
#         if self.cleaned_data['tags']:
#             post.tags.add(*self.cleaned_data['tags'])
#
#         return post
from core.widgets import HTMLEdit


class PostCreate(forms.ModelForm):

    class Meta:
        model = Post
        # fields = ('title', 'text', 'tags', 'pegi')
        exclude = ('author', 'is_published', 'image')
        widgets = {
            'title': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'text': HTMLEdit(),
            'tags': forms.widgets.SelectMultiple(attrs={'class': 'form-control'}),
            'pegi': forms.widgets.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(PostCreate, self).__init__(*args, **kwargs)
        # self.fields['tags'].queryset = Tag.objects.all()[:2]
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def save(self, user, commit=True):
        post = super(PostCreate, self).save(commit=False)
        post.author = user
        post.save()

        self.save_m2m()
        return post


class PostAdmin(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': HTMLEdit(),
        }
