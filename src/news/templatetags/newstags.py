# -*- coding: utf-8 -*-
from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext as _
import logging, random
from datetime import datetime
from news import models

log = logging.getLogger(__name__)
register = template.Library()

@register.inclusion_tag('tags/news.html', takes_context=True)
def news_tag(context, limit = None):
    result = context

    qs = models.News.objects.filter(published__lte=datetime.now()).order_by('-published')

    if limit:
        qs = qs[:limit]
    
    result['news'] = qs
    return result

@register.filter
def hash(h, key):
    try:
        val = h[key]
    except IndexError:
        val = None
    return val

def get_common_dict(context):
    """
    Context here is not affected by context processors
    Explicitly process request by context processor
    """
    request = context['request']
    result = common_data(request)
    result['request'] = request
    return result
