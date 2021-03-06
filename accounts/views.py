from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, TemplateView, RedirectView, DetailView, FormView, ListView
from rest_framework import mixins, generics

from accounts.models import Copyright
from music.models import Music
from .forms import CreateUserForm
from .models import User
from .serializer import CopyrightSerializer, UserWorkingProjectsSerializer


class CreateUserView(CreateView):
    template_name = 'accounts/create_user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:accounts_create_done')


class CreateUserDoneView(TemplateView):
    template_name = 'accounts/create_user_done.html'


class UserLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()

        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(UserLoginView, self).form_valid(form)

    def get_success_url(self):
        return super(UserLoginView, self).get_success_url()


class UserLogoutView(RedirectView):
    url = reverse_lazy('home')

    @method_decorator(never_cache)
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)


class UserDetailView(DetailView):
    template_name = 'accounts/mypage.html'
    model = User
    pk_url_kwarg = 'account_id'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_music_list'] = self.request.user.music_owner.all()
        # context['user_contrib_music_list'] = self.request.user.music_contributor.all()
        return context


class CopyrightAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    object = Copyright.objects.all()
    serializer_class = CopyrightSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CopyrightTemplateView(TemplateView):
    template_name = 'accounts/copyright.html'

    def get_context_data(self, **kwargs):
        context = super(CopyrightTemplateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class UserWorkingProjects(mixins.ListModelMixin, generics.GenericAPIView):

    serializer_class = UserWorkingProjectsSerializer

    def get_queryset(self):
        queryset = Music.objects.filter(owner=self.request.user, contributor=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserWorkingProjectsListView(ListView):
    template_name = 'accounts/user_working_projects.html'
    model = Music
    pk_url_kwarg = 'account_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserWorkingProjectsListView, self).get_context_data(object_list=None, **kwargs)
        context['working_music_list'] = self.request.user.music_owner.all()
        return context


class MyPageListTemplateView(TemplateView):
    template_name = 'accounts/mypage_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyPageListTemplateView, self).get_context_data(**kwargs)
        context['account_id'] = self.request.user.id
        return context


class UserLikedMusicListView(ListView):
    template_name = 'accounts/user_liked_music.html'
    model = Music
    context_object_name = 'user_liked_music_list'
    pk_url_kwarg = 'account_id'

    def get(self, request, *args, **kwargs):
        return super(UserLikedMusicListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = User.objects.get(id=user_id).music.all()
        return queryset
