# coding=utf-8
from __future__ import unicode_literals

import sys

from six.moves import reload_module

from django.conf import settings
from django.contrib import admin
from redirect.models import Redirect
from redirect import urls


class RedirectAdmin(admin.ModelAdmin):
    list_display = ['from_url', 'to_url', 'site', 'status']
    list_filter = ['internal']

    def save_model(self, request, object, form, change):
        instance = form.save()
        # for sites that are not in debug mode reload
        # the dynamic urls, i'm not sure if this is the
        # best way though
        if settings.ROOT_URLCONF in sys.modules:
            reload_module(sys.modules[settings.ROOT_URLCONF])
        reload_module(urls)
        return instance

    def changelist_view(self, request, extra_context=None):
        if 'internal__exact' not in request.GET:
            request.GET = request.GET.copy()
            request.GET.update({'internal__exact': 0})
        return super(RedirectAdmin, self).changelist_view(request, extra_context)

admin.site.register(Redirect, RedirectAdmin)
