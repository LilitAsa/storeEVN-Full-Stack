from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("main.urls","mains"), namespace="main")),
    path("cart/", include(("cart.urls","cart"), namespace="cart")),
    path("users/", include(("users.urls","users"), namespace="users")),
    path("orders/", include(("orders.urls","orders"), namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)