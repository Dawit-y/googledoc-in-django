from django.shortcuts import render
from .forms import DocumentForm



def add_collaborator(request):
    pass





def home(request):
    
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST)

        print(request.POST)
    return render(request, 'core/home.html', {'form' : form})