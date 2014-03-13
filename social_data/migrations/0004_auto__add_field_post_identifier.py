# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.identifier'
        db.add_column(u'social_data_post', 'identifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=512),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.identifier'
        db.delete_column(u'social_data_post', 'identifier')


    models = {
        u'social_data.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['social_data.Service']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'social_data.service': {
            'Meta': {'object_name': 'Service'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['social_data']