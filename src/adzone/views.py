# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from __future__ import absolute_import

from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from adzone.models import AdBase
from adzone.models import AdClick


def ad_view(request, id):
    """ Record the click in the database, then redirect to ad url """
    ad = get_object_or_404(AdBase, id=id)

    click = AdClick.objects.create(
        ad=ad, click_date=datetime.now(), source_ip=request.META.get("REMOTE_ADDR", "")
    )
    click.save()

    redirect_url = ad.url
    if not redirect_url.startswith("http://"):
        # Add http:// to the url so that the browser redirects correctly
        redirect_url = "http://" + redirect_url

    return HttpResponseRedirect(redirect_url)
