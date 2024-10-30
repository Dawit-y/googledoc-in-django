from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Document, User
from .forms import DocumentForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    documents = Document.objects.filter(Q(author = request.user) | Q(collaborators = request.user))
    editor = DocumentForm()
    if request.method == "POST":
        doc = Document.objects.create(author=request.user)
        if doc:
            return redirect("new_document", id = doc.id)
    return render(request, 'core/home.html', {'documents' : documents, "editor" : editor})

def document(request, id):
    editor_form = DocumentForm()
    doc = get_object_or_404(Document, id=id) 
    author = doc.author
    collaborators = doc.collaborators.all()
    users = User.objects.exclude(id = author.id)
    if collaborators:
        users = User.objects.exclude(id__in=[author.id] + [collaborator.id for collaborator in collaborators])
    
    if request.method == "POST":
        collab_id = request.POST.get("collab")
        collab = get_object_or_404(User, id = collab_id)
        doc.collaborators.add(collab)
        doc.save()
    
    return render(request, 'core/document.html', {'new_collaborators': users, "collaborators" : collaborators, "doc" : doc, "editor_form": editor_form}) 


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            return redirect("home")  # Redirect to home page or any other success page
        else:
            # Show error message if authentication fails
            messages.error(request, "Invalid email or password.")
    
    return render(request, "core/login.html")
