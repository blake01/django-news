from django.contrib import admin
from news.models import get_article_model

model = get_article_model()
admin.site.register(model)
