from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Review, Ticket, User, UserFollows

admin.site.register(User, UserAdmin)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
