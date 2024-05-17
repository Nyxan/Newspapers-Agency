from django.urls import path
from .views import (
    index,
    RedactorListView,
    TopicListView,
    NewspapersListView,
    RedactorDetailView,
    NewspaperDetailView,
    RedactorDelete,
    register, RedactorUpdate, create_newspaper
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/",
         RedactorDetailView.as_view(),
         name="redactor-detail"),
    path(
        "drivers/<int:pk>/update/",
        RedactorUpdate.as_view(),
        name="redactor-update",
    ),
    path('redactor/<int:pk>/delete/', RedactorDelete.as_view(), name='redactor-delete'),
    path("newspapers/", NewspapersListView.as_view(), name="newspaper-list"),
    path("newspaper/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path('newspapers/create/', create_newspaper, name='create-newspaper'),

    path("topics/", TopicListView.as_view(), name="topic-list"),
    path('register/', register, name='register')
]
app_name = "board"