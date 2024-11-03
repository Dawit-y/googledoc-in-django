from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Document, User
from .forms import DocumentForm, LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.author = request.user
            document.name = request.POST.get("name") 
            document.save()
            return redirect('document', id=document.id)
    else:
        form = DocumentForm()

    return render(request, 'core/home.html', {'form': form})

def document(request, id):
    doc = get_object_or_404(Document, id=id) 
    editor_form = DocumentForm(instance=doc)
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
    
    return render(request, 'core/document.html', {'new_collaborators': users, "collaborators" : collaborators, "doc" : doc, "editor_form": editor_form, 'document_id': id}) 


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = authenticate(request, username=email, password=password)
        except:
            messages.error(request, "Invalid email or password.")
        
        if user is not None:
            # Login the user
            login(request, user)
            return redirect("home")  # Redirect to home page or any other success page
        else:
            # Show error message if authentication fails
            messages.error(request, "Invalid email or password.")
    
    return render(request, "core/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            # You can redirect to a login page or home page after successful signup
            return redirect('login')
        else:
            # If the form is invalid, it will automatically contain error messages
            return render(request, 'core/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})