# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.image'
        db.add_column(u'news_article', 'image',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['society.LibraryImage']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.image'
        db.delete_column(u'news_article', 'image_id')


    models = {
        u'news.article': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['society.LibraryImage']"}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'title'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'society.libraryimage': {
            'Meta': {'ordering': "['-upload_date']", 'object_name': 'LibraryImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']