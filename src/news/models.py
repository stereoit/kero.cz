# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class News(models.Model):
    title = models.CharField(_(u'title'), max_length=255)
    slug = models.SlugField(_(u'slug'), max_length=255)
    text = models.TextField(_('text'))
    #text = RichTextField(_('text'))
    published = models.DateTimeField(_(u'published'), null=True, blank=True)
    published_by = models.CharField(_(u'author'), max_length=255, null=True, blank=False)

    class Meta:
        verbose_name = _(u'News')
        verbose_name_plural = _(u'News')
        ordering = ['-published']
        get_latest_by = 'published'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news.detail', kwargs={'slug': self.slug})


