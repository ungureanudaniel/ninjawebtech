from django.contrib import admin
from .models import About, Service, Portfolio, TeamMember, Logo, Email, Review, Skill, ProjectCategory, NewsletterUser, Pricing, PricingFeatures, Post
class AboutAdmin(admin.ModelAdmin):
     list_display =  ['title', 'text', 'image', 'active']

class EmailAdmin(admin.ModelAdmin):
     list_display =  ['contact_email', 'contact_subject', 'contact_message', 'contact_author', 'timestamp']

class ServiceAdmin(admin.ModelAdmin):
     list_display =  ['title', 'text', 'thumbnail']
     # prepopulated_fields = {'slug': ('title',), }

class ProjectCategoryAdmin(admin.ModelAdmin):
     list_display =  ['title']
     # prepopulated_fields = {'slug': ('title',), }

class SkillAdmin(admin.ModelAdmin):
     list_display =  ['title', 'percent']
     # prepopulated_fields = {'slug': ('title',), }

class PortfolioAdmin(admin.ModelAdmin):
     list_display =  ['title', 'short_description', 'link', 'start_date', 'end_date', 'category', 'author', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image6', 'image7']
     # prepopulated_fields = {'slug': ('title',), }

class TeamMemberAdmin(admin.ModelAdmin):
     list_display =  ['first_name', 'last_name', 'job', 'email', 'phone', 'insta', 'twitter', 'linkedin', 'photo']

class ReviewAdmin(admin.ModelAdmin):
     list_display =  ['author', 'content', 'date_posted', 'active']

class LogoAdmin(admin.ModelAdmin):
     list_display =  ['text', 'photo']


class NewsletterUserAdmin(admin.ModelAdmin):
     list_display =  ['email', 'conf_number', 'confirmed', 'timestamp']

class PricingFeaturesAdmin(admin.ModelAdmin):
    list_display =  ['feature']

class PricingAdmin(admin.ModelAdmin):
    list_display =  ['category', 'price', 'highlighted']

class PostAdmin(admin.ModelAdmin):
    list_display =  ['title', 'text', 'featured', 'status', 'created_date', 'slug']
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(About, AboutAdmin)
admin.site.register(PricingFeatures, PricingFeaturesAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(NewsletterUser, NewsletterUserAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Review, ReviewAdmin)
