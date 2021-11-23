from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import truncatechars
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

class NewsletterUser(models.Model):
    email = models.CharField(max_length=40)
    conf_number = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.email)

class ProjectCategory(models.Model):
    title = models.CharField(max_length=30)
    # slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(ProjectCategory, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

class About(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='about')
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.title)

class Service(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='services', blank=True)
    # slug = models.SlugField(default="-", max_length=255, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

class PricingFeatures(models.Model):
    feature_en = models.CharField(max_length=30)
    feature_de = models.CharField(max_length=30)
    feature_ro = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.feature_en)

class Pricing(models.Model):
    # features = PricingFeatures.objects.all().values_list('feature', 'feature')
    # features_list = []
    #
    # for item in features:
    #     features_list.append(item)

    category = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    features = models.ManyToManyField(PricingFeatures, blank=True, max_length=30)
    highlighted = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.category)


class Skill(models.Model):
    title = models.CharField(max_length=30)
    percent = models.IntegerField(blank=True, null=True)
    # slug = models.SlugField(default="", max_length=255, unique=True)
    def __str__(self):
        return '{}'.format(self.title)

class WhyChooseUs(models.Model):
    figures = models.CharField(max_length=30)
    reason = RichTextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.reason)

class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    category = models.ForeignKey(ProjectCategory, related_name='category', on_delete=models.SET_NULL, blank=True, null=True)
    author = models.CharField(max_length=30)
    link = models.CharField(max_length=50, blank=True, null=True, default="")
    image1 = models.ImageField(upload_to='portfolio')
    image2 = models.ImageField(upload_to='portfolio', blank=True)
    image3 = models.ImageField(upload_to='portfolio', blank=True)
    image4 = models.ImageField(upload_to='portfolio', blank=True)
    image5 = models.ImageField(upload_to='portfolio', blank=True)
    image6 = models.ImageField(upload_to='portfolio', blank=True)
    image7 = models.ImageField(upload_to='portfolio', blank=True)
    # slug = models.SlugField(default="", max_length=255, unique=True)
    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    class Meta:
        ordering = ["-end_date"]

    def __str__(self):
        return '{}'.format(self.title)

class PortfolioTags(models.Model):
    name = models.CharField(max_length=30)
    project = models.ManyToManyField(Portfolio, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
#-------------------------COMMENTS / REVIEWS MODEL------------------------------
class Review(models.Model):
    author = models.CharField(max_length=300)
    content = RichTextField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.author)


#---------------------------TEAM MEMBERS AND THEIR INFO-------------------------
class TeamMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job = models.CharField(max_length=60, default='python developer')
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    insta = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='')

    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)

#-------------------------COMMENTS / REVIEWS MODEL------------------------------
class Logo(models.Model):
    text = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='logo')


    def __str__(self):
        return '{}'.format(self.author)


#----------------------CONTACT FORM MESSAGES---------------------------
class Email(models.Model):
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=200, default='')
    contact_message = RichTextField(blank=True, null=True)
    contact_author = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.contact_author)


#----------------------CONTACT FORM MESSAGES---------------------------
# class ContactData(models.Model):
#     email = models.EmailField()
#     address = models.TextField(max_length=200, default='')
#     phone = models.CharField(max_length=200, default='')
#
#     class Meta:
#         verbose_name = "Contact Data"
#         verbose_name_plural = "Contact Data"
#
#     def __str__(self):
#         return '{}'.format(self.email)

#----------------------------------THE CATEGORY MODEL-------------------------
class PostCategory(models.Model):
    title = models.CharField(max_length=30)
    # slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(PostCategory, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)
#----------------------------------THE POST MODEL----------------------------
class Post(models.Model):
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_image', blank=True)
    text = RichTextField(blank=True, null=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='postcategory')
    comment_count = models.IntegerField(default=0)
    # views_count = models.IntegerField(default=0)
    featured = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})
        #return reverse('home')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def month_published(self):
        return self.created_date.strftime('%b %Y')

    def post_count(self):
        return self.pk.count()

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class BlogTag(models.Model):
    name = models.CharField(max_length=30)
    post = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
