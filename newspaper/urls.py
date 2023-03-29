from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

app_name = "newspaper"


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("redactor/create/", views.RedactorCreateView.as_view(), name="redactor-create"),
    path("topics/", views.TopicListView.as_view(), name="topic-list"),
    path("topics/create/", views.TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", views.TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", views.TopicDeleteView.as_view(), name="topic-delete"),
    path("topics/<int:pk>/", views.TopicDetailView.as_view(), name="topic-detail"),
    path("newspapers/create/", views.NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", views.NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", views.NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("newspapers/", views.NewspaperListView.as_view(), name="newspaper-list"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
