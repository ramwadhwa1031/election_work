from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm,UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import GuestEmail

# Register your models here.
User=get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'admin')
    list_filter = ('admin','staff', 'active')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname',)}),
        ('Permissions', {'fields': ('admin','staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

#class UserAdmin(admin.ModelAdmin):
#    search_fields =['phone']
#    form=UserAdminChangeForm
#    add_form=UserAdminCreationForm

    #class Meta:
    #    model=User

#admin.site.register(User, UserAdmin)

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields =['phone']
    class Meta:
        model=GuestEmail

admin.site.register(GuestEmail,GuestEmailAdmin)
