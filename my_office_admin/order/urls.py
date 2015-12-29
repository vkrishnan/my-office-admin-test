from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
                url(r'^$', views.main_page),
                url(r'^user/(\w+)/$', views.user_page),
                url(r'^register/$', views.register_page, name='register'),
                url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),
                url(r'^login/$', 'django.contrib.auth.views.login'),
                url(r'^logout/$', views.logout_page),
              ]