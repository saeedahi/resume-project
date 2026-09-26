from django.contrib import admin
from home import models

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'score']
    list_editable = ['score']


class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'score']
    list_editable = ['score']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category']


admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Tools, ToolAdmin)
admin.site.register(models.Projects)
admin.site.register(models.TimeLineRoad)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ContactUsModel)
admin.site.register(models.SocialLinks)