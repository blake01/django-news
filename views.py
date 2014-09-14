from django.views.generic import DetailView, ListView
from django.db.models.loading import get_model
from django.conf import settings
from news.models import Article


class ActiveArticlesMixin(object):
    """Retrieve the appropriate model (models.Article or a subclass)
    for use in the views below"""

    def get_queryset(self):
        app = getattr(settings, 'NEWS_APP', 'news')
        model_name = getattr(settings, 'NEWS_MODEL', 'Article')
        model = get_model(app, model_name)
        assert(issubclass(model, Article))
        return model.objects.active()


class NewsListView(ActiveArticlesMixin, ListView):
    context_object_name = 'articles'


class NewsArchiveView(NewsListView):
    def get_queryset(self):
        qs = super(NewsArchiveView, self).get_queryset()
        return qs.filter(date__year=self.kwargs['year'])


class NewsDetailView(ActiveArticlesMixin, DetailView):
    context_object_name = 'article'
