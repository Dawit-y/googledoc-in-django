from .models import Document
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from tinymce.widgets import TinyMCE

class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('body',)
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''  # Remove the label