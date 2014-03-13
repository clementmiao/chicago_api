# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'social_data_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'social_data', ['Service'])

        # Adding model 'Post'
        db.create_table(u'social_data_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social_data.Service'])),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'social_data', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'social_data_service')

        # Deleting model 'Post'
        db.delete_table(u'social_data_post')


    models = {
        u'social_data.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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