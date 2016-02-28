from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
try:
    # Django <1.7
    from django.db.models.loading import get_model
except ImportError:
    # Django 1.7+
    from django.apps import apps
    get_model = apps.get_model
from django.conf import settings
from autoslug import AutoSlugField


class ArticleManager(models.Manager):

    def active(self):
        now = timezone.now()
        qs = super(ArticleManager, self).get_queryset()
        qs = qs.filter(live=True)
        return qs.filter(date__lte=now.date())

    def draft(self):
        qs = super(ArticleManager, self).get_queryset()
        return qs.filter(live=False)

    def pending(self):
        now = timezone.now()
        qs = super(ArticleManager, self).get_queryset()
        qs = qs.filter(live=True)
        return qs.filter(date__gt=now.date())

    def latest(self, count=1):
        if count == 1:
            return self.active().first()
        else:
            try:
                return self.active()[:count]
            except IndexError:
                # Return all articles if there are fewer than 'count'.
                return self.active()


class ArticleBase(models.Model):
    """
    Article is a bulletin with a title, date and content.
    It may or not be live.
    Forms the basis of blog posts, news articles and message board posts.
    """
    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='title', unique=True)
    date = models.DateField()
    content = models.TextField()
    live = models.BooleanField(
        help_text="Only live sites with dates today or in the past will be shown.",
        default=True,
    )
    objects = ArticleManager()

    def __unicode__(self):
        return '%s - %s'%(self.title, self.date)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    @property
    def date_str(self):
        """String representation of the date, e.g. Saturday 07 December 13"""
        return self.date.strftime('%A %d %B %y')

    class Meta:
        ordering = ['-date']
        abstract = True


class Article(ArticleBase):
    pass


def get_article_model():
    app = getattr(settings, 'NEWS_APP', 'news')
    model_name = getattr(settings, 'NEWS_MODEL', 'Article')
    model = get_model(app, model_name)
    return model
