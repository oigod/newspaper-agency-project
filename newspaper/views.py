from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import RedactorCreationForm
from newspaper.models import Redactor, Topic


class IndexView(generic.FormView):
    template_name = "newspaper/index/index.html"
    form_class = AuthenticationForm
    success_url = "newspaper:topic-list"


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    template_name = "newspaper/registration/redactor_registration.html"
    success_url = "/"


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper/newspaper_lists/topic_list.html"
    paginate_by = 5


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/newspaper_forms/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    template_name = "newspaper/newspaper_details/topic_detail.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "newspaper/newspaper_forms/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "newspaper/newspaper_confirms/topic_confirm_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")
