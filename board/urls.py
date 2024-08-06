from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from board.views import (
    index,
    RedactorListView,
    TopicListView,
    NewspapersListView,
    RedactorDetailView,
    NewspaperDetailView,
    RedactorDelete,
    RedactorUpdate,
    add_comment,
    NewspaperCreateView,
    TopicCreateView,
    RedactorCreateView,
    TopicDetailView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicUpdateView,
    TopicDeleteView,
    newspaper_search,
)

urlpatterns = [
                  path("", index, name="index"),
                  path("redactors/", RedactorListView.as_view(), name="redactor-list"),
                  path(
                      "redactors/<int:pk>/",
                      RedactorDetailView.as_view(),
                      name="redactor-detail"),
                  path(
                      "redactor/<int:pk>/update/",
                      RedactorUpdate.as_view(),
                      name="redactor-update",
                  ),
                  path(
                      "redactor/<int:pk>/delete/",
                      RedactorDelete.as_view(),
                      name="redactor-delete"),
                  path(
                      "redactor/create/",
                      RedactorCreateView.as_view(),
                      name="redactor-create"),
                  path("newspapers/", NewspapersListView.as_view(), name="newspaper-list"),
                  path(
                      "newspaper/<int:pk>/",
                      NewspaperDetailView.as_view(),
                      name="newspaper-detail"),
                  path(
                      "newspapers/create/",
                      NewspaperCreateView.as_view(),
                      name="newspaper-create"
                  ),
                  path(
                      "newspaper/<int:pk>/update/",
                      NewspaperUpdateView.as_view(),
                      name="newspaper-update",
                  ),
                  path(
                      "newspaper/<int:pk>/delete/",
                      NewspaperDeleteView.as_view(),
                      name="newspaper-delete",
                  ),
                  path("topics/", TopicListView.as_view(), name="topic-list"),
                  path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
                  path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
                  path(
                      "manufacturers/<int:pk>/update/",
                      TopicUpdateView.as_view(),
                      name="topic-update",
                  ),
                  path(
                      "manufacturers/<int:pk>/delete/",
                      TopicDeleteView.as_view(),
                      name="topic-delete",
                  ),
                  path(
                      "newspaper/<int:newspaper_id>/add_comment/",
                      add_comment,
                      name="add-comment"
                  ),
                  path("search/", newspaper_search, name="newspaper-search"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
app_name = "board"
