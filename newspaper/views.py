from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import views as auth_views

from newspaper.forms import RedactorCreationForm, NewspaperForm, NewspaperSearchForm, TopicSearchForm, \
    RedactorUpdateForm
from newspaper.models import Redactor, Topic, Newspaper


@login_required(login_url="/sign-in/")
def index(request):
    """View function for the home page of the site."""

    count_redactors = Redactor.objects.count()
    count_newspapers = Newspaper.objects.count()
    count_topics = Topic.objects.count()

    count_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = count_visits + 1

    context = {
        "count_redactors": count_redactors,
        "count_newspapers": count_newspapers,
        "count_topics": count_topics,
        "count_visits": count_visits + 1,
    }

    return render(request, "newspaper/index/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/newspaper_lists/topic_list.html"
    paginate_by = 4
    login_url = "/sign-in/"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        context["search_form"] = TopicSearchForm()

        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/newspaper_forms/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")
    login_url = "/sign-in/"


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    template_name = "newspaper/newspaper_details/topic_detail.html"
    login_url = "/sign-in/"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/newspaper_forms/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")
    login_url = "/sign-in/"


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "newspaper/newspaper_confirms/topic_confirm_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")
    login_url = "/sign-in/"


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "newspaper/newspaper_lists/newspaper_list.html"
    paginate_by = 4
    login_url = "/sign-in/"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)

        context["search_form"] = NewspaperSearchForm()

        return context

    def get_queryset(self):
        queryset = Newspaper.objects.select_related("topic")
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_details/newspaper_detail.html"
    login_url = "/sign-in/"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = NewspaperForm
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_forms/newspaper_form.html"
    login_url = "/sign-in/"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_forms/newspaper_form.html"
    login_url = "/sign-in/"


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")
    template_name = "newspaper/newspaper_confirms/newspaper_confirm_delete.html"
    login_url = "/sign-in/"


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    context_object_name = "redactor"
    template_name = "newspaper/newspaper_details/redactor_detail.html"
    login_url = "/sign-in/"


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "newspaper/newspaper_lists/redactor_list.html"
    paginate_by = 5
    login_url = "/sign-in/"

    class Meta:
        ordering = ["name"]


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = "/"
    template_name = "newspaper/newspaper_confirms/redactor_confirm_delete.html"
    login_url = "/sign-in/"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = RedactorUpdateForm
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")

    template_name = "newspaper/newspaper_forms/redactor_form.html"
    login_url = "/sign-in/"


class LoginView(auth_views.LoginView):
    template_name = "registration/page-sign-in.html"
    success_url = reverse_lazy("newspaper:index")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy("newspaper:sign-in")
    template_name = "registration/page-sign-in.html"
    login_url = "/sign-in/"


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    template_name = "registration/page-sign-up.html"
    success_url = reverse_lazy("newspaper:index")

