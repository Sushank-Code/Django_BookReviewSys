from django.contrib import admin
from book_app.models import BookData

# Register your models here.
@admin.register(BookData)
class BookDataAdmin (admin.ModelAdmin):
    list_display=('id','title','author','genre')
    list_display_links = ('title',)