from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.conf import settings
import os
import requests
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models import Sum
import itertools
import datetime
import random
from django.utils.html import strip_tags
from django.contrib import messages
from .models import About, Service, TeamMember, Skill, Review, ProjectCategory, NewsletterUser,\
 Pricing, Post, Email, PostCategory, Portfolio, PortfolioTags, BlogTag, Comment
from .forms import CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CaptchaForm
from django.views.decorators.csrf import csrf_protect
from hitcount.views import HitCountDetailView
from django.views.generic import ListView, MonthArchiveView
from django.views.generic.edit import FormMixin
# def set_language(request):
#     if request.GET.has_key('language_id'):  # Set language in Session variable
#         # Redirect to home
#         request.session['language_id'] = request.GET['language_id']
#     return HttpResponseRedirect('/')

#-----------------------GENERATE RANDOM SUBSCRIBER ID--------------------------
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


#---------------------------------------------------------------------HOME VIEW
@csrf_protect
def homeview(request):
    template = 'ninjawebtech_app/index9.html'
    #--------------------------------------------------------------------ABOUT

    #--------------------------------------------------------------------SKILLS
    skills = Skill.objects.all()
    #-------------------------------------------------------------------REVIEWS
    reviews = Review.objects.filter(approved=True)
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

    form = CaptchaForm(request.POST)
    if request.method == "POST":
        #----------------contact input- ------------------------------------
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        #------------newsletter input -------------------------------
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
                        "skills": skills,
                        "reviews": reviews,
                        "price_plans": price_plans,
                        "blog_posts": blog_posts,
                        "feat": feat,
                        "form": form,
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
                    "skills": skills,
                    "reviews": reviews,
                    "price_plans": price_plans,
                    "blog_posts": blog_posts,
                    "feat": feat,
                    "form": form,

                }
                return render(request, template, context)

        elif message_email:

            if form.is_valid():
                try:
                    #----------------create database entry with contact data----
                    new_contact = Email(contact_email=message_email, contact_subject = 'New message', contact_author = message_name, contact_message = message, timestamp=datetime.datetime.now())
                    #-------------------------save the contact data to databse--
                    new_contact.save()
                    #----------------send the email to destination-------------
                    send_mail(message_name, message, message_email, ['danielungureanu531@gmail.com'])
                    messages.success(request, "Thank you for writting me {}! I will answer ASAP.".format(message_name))
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/#contact')
            else:
                messages.warning(request, "Invalid captcha! Please try again.")
                return HttpResponseRedirect('/#contact')
            context = {
                "first_three_services": first_three_services,
                "last_three_services": last_three_services,
                "portfolio_category": portfolio_category,
                "portfolio": portfolio,
                "skills": skills,
                "reviews": reviews,
                "price_plans": price_plans,
                "blog_posts": blog_posts,
                "feat": feat,
                "form": form,

            }

            return render(request, template, context)
        else:
            context = {
                "first_three_services": first_three_services,
                "last_three_services": last_three_services,
                "portfolio_category": portfolio_category,
                "portfolio": portfolio,
                "skills": skills,
                "reviews": reviews,
                "price_plans": price_plans,
                "blog_posts": blog_posts,
                "feat": feat,
                "form": form,
            }
            return render(request, template, context)
    else:
        context = {
            "first_three_services": first_three_services,
            "last_three_services": last_three_services,
            "portfolio_category": portfolio_category,
            "portfolio": portfolio,
            "skills": skills,
            "reviews": reviews,
            "price_plans": price_plans,
            "blog_posts": blog_posts,
            "feat": feat,
            "form": form,
        }
        return render(request, template, context)

#--------------------------------------------------------------------REVIEW VIEW
@csrf_protect
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

    context = {}
    return render(request, template, context)

def hide_review_view(request, pk):
    rev = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        rev.approved = False
        rev.save()
        return redirect('/#hide_review_redirect')

    context = {"rev":rev}
    return render(request, template, context)

#---------------------------strip month and year -----------------------------
def strip_date(request):
    date = datetime.datetime.strptime(request, "%Y-%m-%d")
    return date


#--------------------------------------------------------------------BLOG VIEW
# @csrf_protect
# def bloglistview(request):
#     count_posts = []
#     template = 'ninjawebtech_app/blog_list.html'
#     categories = PostCategory.objects.all()
#     blog_posts = Post.objects.all()
#
#     qs = Post.objects.values('created_date').values('created_date')
#     grouped = itertools.groupby(qs, lambda d: d.get('created_date').strftime('%b %Y'))
#     # [(day, len(list(this_day))) for day, this_day in grouped]
#     for k, g in grouped:
#         count_posts.append([k, sum(1 for _ in g)])
#     context = {
#         "categories": categories,
#         "blog_posts":blog_posts,
#         "count_posts": count_posts,
#     }
#     return render(request, template, context)
class BlogList(ListView):
    template_name = "ninjawebtech_app/blog_list.html"
    context_object_name = "bloglist"
    paginate_by = 2 # add this
    model = Post

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context.update({
            # ----------- recent posts ---------------------------------------
            'recent_posts': Post.objects.all().order_by("-created_date")[:2],
            # ----------- all posts by date-----------------------------------
            'blog_posts': Post.objects.all().order_by("-created_date"),
        })
        return context
#---------------------------------------------------------------BLOG DETAIL VIEW
class PostDetailView(HitCountDetailView, FormMixin):
    model = Post
    template_name = 'ninjawebtech_app/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    form_class = CommentForm
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        form2 = self.get_form()
        comm = Comment.objects.filter(post=Post.objects.get(slug=self.object.slug))
        context.update({
        # ----------- most viewed posts---------------------------------------
        'popular_posts': posts.order_by('-hit_count_generic__hits')[:3],
        # ----------- comments -------------------------------------------
        'comm': comm,
        'comments': comm.count(),
        # ----------- recent posts ---------------------------------------
        'recent_posts': posts.order_by("-created_date")[:2],
        # ----------- most posts  ---------------------------------------
        'posts': posts,
        'form2': form2,
        'form': CaptchaForm()
        })
        return context
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     f = CommentForm(request.POST)
    #     if f.is_valid():
    #         print(f)
    #         f.save()
    #         messages.success(request, f'Your comment has been saved.')
    #     return redirect('.')



    # def get_queryset(self):
    #     self.p = get_object_or_404(Post, title=self.kwargs['post'])
    #     return Comment.objects.filter(post=self.p)
class ArticleMonthArchiveView(MonthArchiveView):

    date_field = "created_date"
    allow_future = True
    template_name = "ninjawebtech_app/blog_list.html"
    context_object_name = "bloglist"
    paginate_by = 2 # add this
    def get_queryset(self):
        blog_posts = Post.objects.all().order_by("-created_date")
        return blog_posts

    def get_context_data(self, **kwargs):
        context = super(ArticleMonthArchiveView, self).get_context_data(**kwargs)
        context.update({
            # ----------- recent posts ---------------------------------------
            'recent_posts': Post.objects.all().order_by("-created_date")[:2],
            # ----------- all posts by date-----------------------------------
            'blog_posts': Post.objects.all().order_by("-created_date"),
        })
        return context
#---------------------------------------------------------------BLOG SEARCH VIEW
class SearchList(ListView):
    template_name = "ninjawebtech_app/search_list.html"
    paginate_by = 2 # add this
    def get_queryset(self):
        if request.method == "GET":
            query = self.request.GET.get("q")
            try:
                results = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query) | Q(category__icontains=query))
        return results

#---------------------------------------------------------------    CONTACT VIEW
@csrf_protect
def ContactView(request):
    template_name = 'ninjawebtech_app/contact.html'
    categories = Category.objects.all()
    #--------------logo------------------------------
    # logos = Logo.objects.filter(status='active')
    form = CaptchaForm(request.POST)
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')
        #send email
        if message and message_name and message_email:
            if form.is_valid():
                try:
                    send_mail(
                    message_name,
                    message,
                    message_email,
                    ['danielungureanu531@gmail.com']
                    )
                    messages.success(request, "Thank you for writting me {}! I will answer ASAP.".format(message_name))
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/')
            else:

                messages.warning(request, "Failed! Please fill in the captcha field again!")
                return HttpResponseRedirect('/contact/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

        render(request, template_name, {'message_name': message_name, 'categories': categories, 'form': form,})
    else:
        return render(request, template_name, {'categories': categories, 'form': form})





@csrf_protect
def subscription_conf_view(request):
    template = 'ninjawebtech_app/subscription_conf.html'

    try:
        sub = NewsletterUser.objects.get(email=request.GET['email'])
        if sub.conf_number == request.GET['conf_number']:
            try:
                sub.confirmed = True
                sub.save()
            except:
                messages.warning(request, "Error! Your email cannot be registered. Please contact us at +40757484560")
            return render(request, template, {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, template, {'email': sub.email, 'action': 'denied'})
    except:
        messages.warning(request, "This email already exists in our database!")
        return render(request, template, {})
