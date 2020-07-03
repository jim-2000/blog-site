from django.contrib import admin
from .models import author, catagory , article, comment

# Register your models here.

#author model coustomize
class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]
    class meta:
        Model = author

admin.site.register(author, authorModel)

# catagory customize 
class catagoryModel(admin.ModelAdmin):
    list_display = ["__str__","post_on"]
    search_fields = ["__str__"]
    list_per_page = 20

    class meta:
        Model = catagory

admin.site.register(catagory, catagoryModel)
# article model customize 
class articleModel(admin.ModelAdmin):
    list_display = ["__str__","post_on","post_update"]
    search_fields = ["__str__", "details"]
    list_filter = ["post_on", "catagory"]

    class meta:
        Model = article

admin.site.register(article, articleModel)

# Comment Register & model customize 
class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10

    class meta:
        Model = comment

admin.site.register(comment, commentModel)
