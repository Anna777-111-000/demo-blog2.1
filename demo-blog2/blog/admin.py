from django.contrib import admin

# Register your models here.
from .models import Category, Post, Comment, Like, Donation

#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    ...

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
 #...

#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
 #   ...

#@admin.register(Like)
#class LikeAdmin(admin.ModelAdmin):
 #   ...

#@admin.register(Donation)
#class DonationAdmin(admin.ModelAdmin):
 #   ...

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Donation)

