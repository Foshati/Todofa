from django import forms
from .models import Todo
import datetime


class TodoForms(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    create = forms.DateTimeField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["create"].initial = datetime.datetime.now()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "body", "create")
