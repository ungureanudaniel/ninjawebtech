from django.contrib import admin
from .models import About, Service, Portfolio, TeamMember, Logo, Email, ContactData, Review, Skill, ProjectCategory

class AboutAdmin(admin.ModelAdmin):
     list_display =  ['title', 'text', 'image', 'active']

class ServiceAdmin(admin.ModelAdmin):
     list_display =  ['title', 'text', 'thumbnail']

class ProjectCategoryAdmin(admin.ModelAdmin):
     list_display =  ['title']

class SkillAdmin(admin.ModelAdmin):
     list_display =  ['title', 'percent']

class PortfolioAdmin(admin.ModelAdmin):
     list_display =  ['title', 'short_description', 'link', 'start_date', 'end_date', 'category', 'author', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image6', 'image7']

class TeamMemberAdmin(admin.ModelAdmin):
     list_display =  ['first_name', 'last_name', 'job', 'email', 'phone', 'insta', 'twitter', 'linkedin', 'photo']

class ReviewAdmin(admin.ModelAdmin):
     list_display =  ['author', 'content', 'date_posted', 'active']

class LogoAdmin(admin.ModelAdmin):
     list_display =  ['text', 'photo']

admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Email)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ContactData)
admin.site.register(Review, ReviewAdmin)
