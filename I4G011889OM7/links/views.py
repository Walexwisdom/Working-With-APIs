from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Link
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from .serializers import LinkSerializer

class LinkListApi(ListView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkCreateApi(CreateView):
   queryset = Link.objects.filter(active=True)
   serializer_class = LinkSerializer


class LinkDetailApi(DetailView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class LinkUpdateApi(UpdateView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class LinkDeleteApi(DeleteView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer