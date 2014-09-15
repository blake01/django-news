from django.views.generic import DetailView, ListView
from news.models import get_article_model


class ActiveArticlesMixin(object):
    """Retrieve the appropriate model (models.Article or a subclass)
    for use in the views below"""

    def get_queryset(self):
        model = get_article_model()
        return model.objects.active()


class NewsListView(ActiveArticlesMixin, ListView):
    context_object_name = 'articles'


class NewsArchiveView(NewsListView):
    def get_queryset(self):
        qs = super(NewsArchiveView, self).get_queryset()
        return qs.filter(date__year=self.kwargs['year'])


class NewsDetailView(ActiveArticlesMixin, DetailView):
    context_object_name = 'article'
