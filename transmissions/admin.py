from django.contrib import admin
from .models import Transmission, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class TransmissionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Comment)
