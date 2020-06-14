from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogHomeView

urlpatterns = [
                  url(r'^artikel/', include('artikel.urls', namespace='artikel')),
                  url(r'^login/', include('login.urls', namespace='login')),
                  url(r'^$', BlogHomeView.as_view(), name='home'),
                  url(r'^admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
