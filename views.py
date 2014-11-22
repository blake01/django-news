from django.views.generic import DetailView, ListView
from endless_pagination.views import AjaxListView
from news.models import get_article_model


class ActiveArticlesMixin(object):
    """Retrieve the appropriate model (models.Article or a subclass)
    for use in the views below"""

    def get_queryset(self):
        model = get_article_model()
        return model.objects.active()


class NewsListView(ActiveArticlesMixin, ListView):
    """Non-ajax version of the view below. Include an appropriate URL
    and we're good to go. """
    context_object_name = 'articles'
    template_name = 'news/article_list.html'


class NewsEndlessListView(ActiveArticlesMixin, AjaxListView):
    """Latest-first list of all news articles, featuring AJAX pagination. """
    context_object_name = 'articles'
    template_name = 'news/article_list_endless.html'
    page_template = 'news/article_list_endless_item.html'


class NewsArchiveView(NewsListView):
    """List view of news stories, filtered by year. """
    def get_queryset(self):
        qs = super(NewsArchiveView, self).get_queryset()
        return qs.filter(date__year=self.kwargs['year'])


class NewsDetailView(ActiveArticlesMixin, DetailView):
    """View a single news article. """
    context_object_name = 'article'
    template_name = 'news/article_detail.html'
