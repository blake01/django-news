"""Script to migrate from one news app to another.
Modify as appropriate and import to run."""

from j29.university.society.models import Article
from news.models import Article as BaseArticle


old = BaseArticle.objects.all()
for x in old:
    a = Article(x.pk, x.title, x.slug, x.date, x.content, x.live)
    a.save()
