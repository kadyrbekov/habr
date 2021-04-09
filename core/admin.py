from django.contrib import admin
from core.models import Article, Author

# Register your models here.

admin.site.register(Author)

class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article

    list_display = ('title', 'author', 'views', 'updated_at')
    list_editable = ('author',)
    list_filter = [] #is_active 
    search_fields = ['title', 'text']

admin.site.register(Article, ArticleAdmin)