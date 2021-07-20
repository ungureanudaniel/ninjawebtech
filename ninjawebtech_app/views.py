from django.shortcuts import render
from django.conf import settings
import os
import datetime
import random
from django.utils.html import strip_tags
from django.contrib import messages
from .models import About, Service, Portfolio, TeamMember, Skill, Review, ProjectCategory, NewsletterUser, Pricing, Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


#-----------------------GENERATE RANDOM SUBSCRIBER ID--------------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


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
    #------------------------------------------------------------------PORTFOLIO
    first_three_services = Service.objects.all()[:3]
    last_three_services = Service.objects.all()[3:]
    #-------------------------------------------------------------------PRICING
    price_plans = Pricing.objects.all()
    feat = Pricing.objects.values_list('features', flat=True)

    #-------------------------------------------------------------------blog
    blog_posts = Post.objects.filter(featured=True)

    print(feat)
    if request.method == "POST":
        newsletter_email = request.POST.get('sub_email')
        if newsletter_email:
            try:
                duplicate = NewsletterUser.objects.get(email=newsletter_email)

                if duplicate:
                    messages.warning(request, "This email already exists in our database!")
                    context = {
                        "first_three_services": first_three_services,
                        "last_three_services": last_three_services,
                        "portfolio_category": portfolio_category,
                        "portfolio": portfolio,
                        'about_us': about_us,
                        "skills": skills,
                        "reviews": reviews,
                        "price_plans": price_plans,
                        "blog_posts": blog_posts,
                        "feat": feat,
                        }
                    return render(request, template, context)
            except:
                sub = NewsletterUser(email=newsletter_email, conf_number=random_digits())
                sub.save()
                messages.success(request, "Please check your email address for a confirmation link!")
                #---------------------send confirmation email settings------
                sub_subject = "Newsletter Ninja WebTECH"
                from_email=settings.FROM_EMAIL
                sub_message = ''
                html_content='Many thanks for subscribing to our newsletter!\
                            To finalize the process please \
                            <a href="{}subscription_confirmation/?email={}&conf_number={}"> click this link \
                            </a>.'.format(request.build_absolute_uri(''), sub.email, sub.conf_number)
                try:
                    send_mail(sub_subject, sub_message, from_email, [sub], html_message=html_content)

                    context = {
                        }

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                # messages.warning(request, "error at except duplicate")
                context = {
                    "first_three_services": first_three_services,
                    "last_three_services": last_three_services,
                    "portfolio_category": portfolio_category,
                    "portfolio": portfolio,
                    'about_us': about_us,
                    "skills": skills,
                    "reviews": reviews,
                    "price_plans": price_plans,
                    "blog_posts": blog_posts,
                    "feat": feat,
                }
                return render(request, template, context)
        else:

            context = {
                "first_three_services": first_three_services,
                "last_three_services": last_three_services,
                "portfolio_category": portfolio_category,
                "portfolio": portfolio,
                'about_us': about_us,
                "skills": skills,
                "reviews": reviews,
                "price_plans": price_plans,
                "blog_posts": blog_posts,
                "feat": feat,
            }
            return HttpResponseRedirect("/")
    else:
        context = {
            "first_three_services": first_three_services,
            "last_three_services": last_three_services,
            "portfolio_category": portfolio_category,
            "portfolio": portfolio,
            'about_us': about_us,
            "skills": skills,
            "reviews": reviews,
            "price_plans": price_plans,
            "blog_posts": blog_posts,
            "feat": feat,
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

#--------------------------------------------------------------------BLOG VIEW
def bloglistview(request):
    template = 'ninjawebtech_app/blog.html'

    context = {

    }
    return render(request, template, context)

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
