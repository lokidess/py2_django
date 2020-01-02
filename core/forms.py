from django import forms

from core.models import Todo


# class CreateTodoForm(forms.Form):
#     text = forms.CharField(widget=forms.widgets.Textarea())
#     priority = forms.ChoiceField(choices=Todo.PRIORITY_CHOICES)
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if len(text) < 20:
#             raise forms.ValidationError('Must be more 20 chars')
#         return text
#
#     def save(self):
#         Todo.objects.create(
#             text=self.cleaned_data['text'],
#             priority=self.cleaned_data['priority']
#         )
# class CreateTodoForm(forms.ModelForm):
#
#     class Meta:
#         model = Todo
#         fields = '__all__'
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if len(text) < 20:
#             raise forms.ValidationError('Must be more 20 chars')
#         return text
