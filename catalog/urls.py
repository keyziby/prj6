from django.urls import path
from catalog.templates.catalog import index_home, index_contact
urlpatterns = [
    path('catalog/', index_contact),
    path('', index_home)
]