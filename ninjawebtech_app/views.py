from django.shortcuts import render
from django.conf import settings
import os
import datetime
import random
from django.utils.html import strip_tags
from django.contrib import messages
from .models import About, Service, Portfolio, TeamMember, Skill, Review, ProjectCategory
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#---------------------------------------------------------------------HOME VIEW
def homeview(request):
    template = 'ninjawebtech_app/index9.html'
    #--------------------------------------------------------------------ABOUT
    about_us = About.objects.filter(active=True)
    #--------------------------------------------------------------------SKILLS
    skills = Skill.objects.all()
    #-------------------------------------------------------------------REVIEWS
    reviews = Review.objects.filter(active=True)
    #------------------------------------------------------------------category
    portfolio_category = ProjectCategory.objects.all()
    #------------------------------------------------------------------PORTFOLIO
    portfolio = Portfolio.objects.all()


    context = {
        "portfolio_category": portfolio_category,
        "portfolio": portfolio,
        'about_us': about_us,
        "skills": skills,
        "reviews": reviews,
    }
    return render(request, template, context)
#-------------------------------------------------------------------CONTACT VIEW

# def contactview(request):
#     template = 'ninjawebtech_app/page-contact.html'
#
#     context = {
#
#     }
#     return render(request, template, context)
#
#--------------------------------------------------------------------REVIEW VIEW
def reviewview(request):
    template = 'ninjawebtech_app/review.html'

    if request.method == "POST":
        user_name = request.POST.get('name')
        user_review = request.POST.get('message')
        if user_name and user_review:
            #-----------------------SAVE IN DATABASE----------------
            new_review = Review(author = user_name, content=user_review, date_posted = datetime.datetime.now())
            new_review.save()
            messages.success(request, "Your review has been sent!")

    context = {

    }
    return render(request, template, context)

# #--------------------------------------------------------------------BLOG VIEW
# def blogview(request):
#     template = 'ninjawebtech_app/blog.html'
#
#     context = {
#
#     }
#     return render(request, template, context)
#
# #------------------------------------------------------------------SERVICES VIEW
# def servicesview(request):
#     template = 'ninjawebtech_app/contact.html'
#
#     context = {
#
#     }
#     return render(request, template, context)
#
# #-----------------------------------------------------------------PORTFOLIO VIEW
# def portfolioview(request):
#     template = 'ninjawebtech_app/content-portfolio-masonry-fullwidth.html'
#
#     context = {
#
#     }
#     return render(request, template, context)
