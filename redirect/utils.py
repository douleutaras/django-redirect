# coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from django.conf import settings
from django.db import connection

from models import Redirect
from views import redirect_to


def get_redirect_patterns():
    """
        Gets the redirect patterns out of the database
        and assigns them to the django patterns object.
    """
    site_id = settings.SITE_ID
    url_list = []
    db_filters = {
        'status': True,
        'site': site_id
    }

    if 'redirect_redirect' in connection.introspection.table_names():
        redirects = Redirect.objects.filter(**db_filters)
    else:
        redirects = []

    for redirect in redirects:
        extra = {}
        pattern = r'^%s$' % redirect.from_url

        extra.update({'url': '%s' % redirect.to_url})

        if redirect.http_status == 302:
            extra.update({'permanent': False})
        url_list.append(url(pattern, redirect_to, extra))

    return url_list
