from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tracker import views

urlpatterns = [
    path('', include('pwa.urls')),

    path('admin/', admin.site.urls),

    path('login/', views.login_view, name='login'),

    path('accounts/', include('allauth.urls')),

    path('', include('tracker.urls')),

    path('', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )