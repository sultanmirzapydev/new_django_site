from django.contrib import admin


from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','is_published', 'date')
	list_display_links = ('title',)

admin.site.register(Blog,BlogAdmin)
