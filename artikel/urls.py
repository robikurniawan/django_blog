from django.conf.urls import url


from .views import (
    ArtikelListView,
    ArtikelDetailView,
    ArtikelCreateView,
    ArtikelManageView,
    ArtikelUpdateView,
    ArtikelDeleteView
)

app_name = 'artikel'

urlpatterns = [

                  url(r'^$', ArtikelListView.as_view(), name='list'),
                  url(r'^tambah/$', ArtikelCreateView.as_view(), name='create'),
                  url(r'^manage/update/(?P<pk>\d+)$', ArtikelUpdateView.as_view(), name='update'),
                  url(r'^manage/delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(), name='delete'),
                  url(r'^manage/$', ArtikelManageView.as_view(), name='manage'),
                  url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
              ]
