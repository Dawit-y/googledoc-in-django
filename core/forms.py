from .models import Document
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('collaborators','body')
        widgets = {
            "body" : CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"
              )
        }

