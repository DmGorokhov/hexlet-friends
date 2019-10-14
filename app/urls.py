from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as lazy

from app.views import contributor, contributors, home, registration, webhook

app_name = 'contributors'
urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path(
        'registration',
        registration.RegistrationView.as_view(),
        name='registration',
    ),
    path(
        'contributors',
        contributors.ListView.as_view(),
        name='contributors_list',
    ),
    path(
        'contributors/<int:pk>',
        contributor.DetailView.as_view(),
        name='contributor_details',
    ),
    path('event-handler', webhook.EventHandler.as_view()),
]

admin.site.index_title = lazy('Hexlet Friends')
admin.site.site_header = lazy('Site administration')
admin.site.site_title = lazy('Site Administration')
