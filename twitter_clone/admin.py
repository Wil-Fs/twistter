from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Twist

#Mix Profile info into User info
class ProfileInLine(admin.StackedInline):
    model = Profile

#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    #Display username
    fields = ["username"]
    inlines = [ProfileInLine]

# Unregister
admin.site.unregister(Group)
admin.site.unregister(User)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Twist)

