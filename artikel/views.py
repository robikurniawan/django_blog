from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .models import Upload

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

# load model
from .models import Artikel
from .forms import ArtikelForm


class ArtikelPerKategori:
    model = Artikel

    def get_latest_artikel_each_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []

        for kategori in kategori_list:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel)
        return queryset


class ArtikelListView(ListView):  # method controller for view
    model = Artikel  # model
    template_name = "artikel/artikel_list.html"  # view location template
    context_object_name = "artikels"  # variabel array
    ordering = ['-published']  # ordering (- desc)

    # paginate_by = 3 #limit

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = "artikel"


@method_decorator(login_required, name='dispatch')
class ArtikelManageView(ListView):
    model = Artikel
    template_name = "artikel/artikel_manage.html"
    context_object_name = "artikel"


@method_decorator(login_required, name='dispatch')
class ArtikelCreateView(SuccessMessageMixin, CreateView):
    form_class = ArtikelForm
    template_name = "artikel/artikel_create.html"
    success_message = " Artikel created successfully"
    success_url = reverse_lazy('artikel:manage')


@method_decorator(login_required, name='dispatch')
class ArtikelDeleteView(SuccessMessageMixin, DeleteView):
    model = Artikel
    form_class = ArtikelForm
    template_name = "artikel/artikel_delete_confirm.html"
    danger_message = " deleted  successfully"
    success_url = reverse_lazy('artikel:manage')

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, self.danger_message)
        return super(ArtikelDeleteView, self).delete(request, *args, **kwargs)


class ArtikelUpdateView(SuccessMessageMixin, UpdateView):
    form_class = ArtikelForm
    model = Artikel
    success_message = " updated created successfully"
    template_name = "artikel/artikel_update.html"
