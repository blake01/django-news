from django.test import TestCase
from django.core.urlresolvers import reverse
from news.models import get_article_model, ArticleBase
import datetime
from autofixture import AutoFixture


Article = get_article_model()


class EmptyDbTestCase(TestCase):
    """Test the app methods with no data in the database."""

    def test_latest_returns_none(self):
        latest = Article.objects.latest()
        self.assertEqual(latest, None)

    def test_article_model_is_subclass(self):
        self.assertTrue(issubclass(Article, ArticleBase))


class NewsTestCase(TestCase):

    def setUp(self):
        """Use autofixture to help set up initial data. """
        field_values_list = [
            {
                'title': "Past Draft",
                'date': datetime.date.today() - datetime.timedelta(days=10),
                'live': False
            },
            {
                'title': "Past Live 1",
                'date': datetime.date(2013, 12, 25),
            },
            {
                'title': "Past Live 2",
                'date': datetime.date.today() - datetime.timedelta(days=7),
            },
            {
                'title': "Past Live 3",
                'date': datetime.date.today() - datetime.timedelta(days=5),
            },
            {
                'title': "Future Draft",
                'date': datetime.date.today() + datetime.timedelta(days=10),
                'live': False
            },
            {
                'title': "Future Live",
                'date': datetime.date.today() + datetime.timedelta(days=10),
                'live': True
            },
        ]
        for f in field_values_list:
            f['slug'] = None
            fixture = AutoFixture(Article, generate_fk=True, field_values=f)
            entry = fixture.create(1)

    def test_autoslug(self):
        l1 = Article.objects.get(title="Past Live 1")
        self.assertEqual(l1.slug, 'past-live-1')

    def test_live_implicitly_true(self):
        l1 = Article.objects.get(title="Past Live 1")
        self.assertTrue(l1.live)

    def test_active_articles_count(self):
        active = Article.objects.active()
        self.assertEqual(active.count(), 3)

    def test_draft_articles_count(self):
        drafts = Article.objects.draft()
        self.assertEqual(drafts.count(), 2)

    def test_pending_articles_count(self):
        pending = Article.objects.pending()
        self.assertEqual(pending.count(), 1)

    def test_get_one_latest(self):
        latest = Article.objects.latest()
        self.assertEqual(latest.title, "Past Live 3")

    def test_get_two_latest(self):
        latest = Article.objects.latest(2)
        self.assertEqual(latest.count(), 2)

    def test_get_excessive_latest(self):
        latest = Article.objects.latest(5)
        self.assertEqual(latest.count(), 3)

    def test_articles_ordered_by_date(self):
        first = Article.objects.active().first()
        last = Article.objects.active().last()
        self.assertEqual(first.title, "Past Live 3")
        self.assertEqual(last.title, "Past Live 1")

    def test_article_date_str(self):
        article = Article.objects.get(title="Past Live 1")
        self.assertEqual(article.date_str, "Wednesday 25 December 13")

    def test_article_list(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

    def test_article_year_archive(self):
        response = self.client.get(
            reverse('article_year_archive', kwargs={'year': '2013'})
        )
        self.assertEqual(response.status_code, 200)

    def test_article_detail(self):
        response = self.client.get(
            reverse('article_detail', kwargs={'slug': 'past-live-1'})
        )
        self.assertEqual(response.status_code, 200)
