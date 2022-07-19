from django.urls import URLPattern, path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', views.inicio, name="Inicio"),
    path('faq', views.faq, name="Faq"),
    path('contacto', views.contacto, name="Contacto"),
    path('about', views.about, name="About"),
    path('blog', views.blog, name="Blog"),
]