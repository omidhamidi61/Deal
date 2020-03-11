from django import forms
from app1.models import WorkersTable, MessagesTable

class WorkersForm(forms.ModelForm):
    class Meta:
        model=WorkersTable
        fields = ['name','username','pssword']

class MessagesForm(forms.ModelForm):
    class Meta:
        model = MessagesTable
        fields = ['sender','title','content','isAccepted']
