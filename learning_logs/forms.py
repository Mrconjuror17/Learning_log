from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry  # Specify the model to use
        fields = ['text']  # Specify the fields to include in the form
        labels = {'text': ''}  # Empty label for 'text' field
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
      