from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('document/<int:id>', views.document, name="new_document"),
    path("login", views.login_view, name="login")
]
