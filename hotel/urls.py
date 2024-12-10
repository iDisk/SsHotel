
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('rooms/', rooms, name='rooms'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
]
