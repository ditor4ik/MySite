from django import forms


class CreateContentView(forms.Form):
    Head = forms.CharField(max_length=100, label="Название книги",
                           widget=forms.TextInput(attrs={'class': 'HeadJQ form-control form-control-lg'}))
    ShortText = forms.CharField(label="Короткое описание книги",
                                widget=forms.Textarea(attrs={'class': 'form-control '
                                                                      'form-control-lg'}))


class CreateComment(forms.Form):
    CommentField = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))