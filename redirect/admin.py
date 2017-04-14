# coding=utf-8
from __future__ import unicode_literals

from django.contrib import admin
from models import Redirect
import urls


class RedirectAdmin(admin.ModelAdmin):
    list_display = ['from_url', 'to_url', 'site', 'status']

    def save_model(self, request, object, form, change):
        instance = form.save()
        # for sites that are not in debug mode reload
        # the dynamic urls, i'm not sure if this is the
        # best way though
        reload(urls)
        return instance

admin.site.register(Redirect, RedirectAdmin)
