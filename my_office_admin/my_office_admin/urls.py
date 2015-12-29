from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
                url(r'^$', 'order.views.main_page'),
                url(r'^user/(\w+)/$', 'order.views.user_page'),
                url(r'^register/$', 'order.views.register_page', name='register'),
                url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),
                url(r'^login/$', 'django.contrib.auth.views.login'),
                url(r'^logout/$', 'order.views.logout_page'),
                url(r'^admin/', include(admin.site.urls)),
              ]
