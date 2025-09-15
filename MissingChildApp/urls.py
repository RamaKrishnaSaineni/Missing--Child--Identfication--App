from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MissingChildApp import views

urlpatterns = [
    # Django default admin (keep it separate)
    path("admin/", admin.site.urls),

    # Home page
    path("", views.Index, name="index"),

    # Public upload
    path("upload/", views.Upload, name="upload"),
    path("upload_action/", views.UploadAction, name="UploadAction"),

    # ✅ Official login (custom, not Django admin)
    path("official-login/", views.OfficialLogin, name="official_login"),

    # Dashboard after login
    path("officialscreen/", views.OfficialScreen, name="officialscreen"),

    # View uploaded children
    path("view/", views.ViewChildren, name="view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)