from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("core.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/workspaces/", include("workspaces.urls")),
    path("api/v1/projects/", include("projects.urls")),
]
