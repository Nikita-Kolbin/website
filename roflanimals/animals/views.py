from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from animals.models import *
from animals.forms import *
from animals.utils import DataMixin


class HomePage(DataMixin, ListView):
    model = Animal
    template_name = 'animals/index.html'
    context_object_name = 'animals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', h1='Это главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Animal.objects.filter(is_published=True)


class Post(DetailView):
    model = Animal
    template_name = 'animals/post.html'
    context_object_name = 'animal'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['animal'].name
        return context


class Category(DataMixin, ListView):
    model = Animal
    template_name = 'animals/index.html'
    context_object_name = 'animals'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['animals'][0].category,
            h1='Категория ' + str(context['animals'][0].category).lower()
        )
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Animal.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)


class ShowForm(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'animals/form.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Форма'
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'animals/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация', reg=True)
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'animals/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход', log=True)
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'animals/about.html', {'title': 'О сайте'})


def login(request):
    return render(request, 'animals/login.html', {'title': 'Login'})


# def category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     context = {
#         'animals': Animal.objects.filter(category_id=category.pk),
#         'title': category.name,
#         'h1': f'Категория {category.name}'
#     }
#     return render(request, 'animals/index.html', context=context)


# def index(request):
#     context = {
#         'animals': Animal.objects.all(),
#         'title': 'Глвная страница',
#         'h1': 'Это главная страница'
#     }
#
#     return render(request, 'animals/index.html', context=context)


# def post(request, post_slug):
#     animal = get_object_or_404(Animal, slug=post_slug)
#     context = {
#         'animal': animal,
#         'title': animal.name
#     }
#     return render(request, 'animals/post.html', context=context)


# def show_form(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'animals/form.html', context={'title': 'Форма', 'form': form})
