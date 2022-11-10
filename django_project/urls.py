from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("backoffice/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("store/", include("store.urls")),
    path("", include("pages.urls")),
    path("unicorn/", include("django_unicorn.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
