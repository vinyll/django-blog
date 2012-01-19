from urls import *
from django.conf import settings

urlpatterns += patterns("",
    url(
        r"^%s/(?P<path>.*)/?$" % settings.STATIC_URL.strip('/'),
        "django.views.static.serve",
        dict(document_root=settings.STATIC_ROOT),
        ),
    (r'^feincms_media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.FEINCMS_ADMIN_MEDIA_LOCATION, 'show_indexes': True}),
    )