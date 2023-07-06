from django.contrib import admin
from .models import Question, Post, Choice, Game, Tag, Author 


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)
    
class GameAdmin(admin.ModelAdmin):
    list_filter = ("tags",)
    
class PostAdmin(admin.ModelAdmin):
    list_filter = ("game",)
    list_display = ("title", "author", "rating", "date",) 
    prepopulated_fields = {"slug": ("title",)}
    

# Register your models here.
admin.site.register(Question)
admin.site.register(Post, PostAdmin)
admin.site.register(Choice)
admin.site.register(Game, GameAdmin)
admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)

