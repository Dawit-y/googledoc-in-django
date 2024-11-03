from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Document, User
from django_summernote.admin import SummernoteModelAdmin

class UserAdmin(BaseUserAdmin):
    # Specify the fields to display in the admin form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Use email as the identifier instead of username
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        # If a new password is set, hash it before saving
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

# Register the custom User model with the custom UserAdmin
class DocumentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

    
admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)
