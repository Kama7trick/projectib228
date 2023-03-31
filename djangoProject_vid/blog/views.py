from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from .models import BirdPost
from .models import MammalsPost
from .models import FishPost


class Bloglist(ListView):
    paginate_by = 5
    model = Post
    template_name = 'home.html'


class BlogBirds(ListView):
    paginate_by = 5
    model = BirdPost
    template_name = 'birds.html'


class BlogMammals(ListView):
    paginate_by = 5
    model = MammalsPost
    template_name = 'mammals.html'


class BlogFish(ListView):
    paginate_by = 5
    model = FishPost
    template_name = 'fish.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BirdsDetailView(DetailView):
    model = BirdPost
    template_name = 'birds_detail.html'


class FishDetailView(DetailView):
    model = FishPost
    template_name = 'fish_detail.html'


class MammalsDetailView(DetailView):
    model = MammalsPost
    template_name = 'mammals_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class Search(ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('q')) or BirdPost.objects.filter(
            title__icontains=self.request.GET.get('q')) or MammalsPost.objects.filter(
            title__icontains=self.request.GET.get('q')) or FishPost.objects.filter(
            title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class ShuePageView(TemplateView):  # Форум
    template_name = 'shue.html'


class ContactPageView(TemplateView):  # Контактная информация
    template_name = 'contact.html'


class GalleryPageView(TemplateView):  # Галерея
    template_name = 'gallery.html'


@login_required
def profile_view(request):
    return render(request, 'profile.html')
