# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.image'
        db.delete_column(u'news_article', 'image_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Article.image'
        raise RuntimeError("Cannot reverse this migration. 'Article.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Article.image'
        db.add_column(u'news_article', 'image',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['society.LibraryImage']),
                      keep_default=False)


    models = {
        u'news.article': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'title'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['news']