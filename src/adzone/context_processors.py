from __future__ import absolute_import


def get_source_ip(request):
    if "REMOTE_ADDR" in request.META:
        return {"from_ip": request.META["REMOTE_ADDR"]}
    else:
        return {}
