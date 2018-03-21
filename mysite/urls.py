from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views as core_views


urlpatterns = [
url(r'^', include('orders.urls', namespace='orders')),
 url(r'^', include('cart.urls', namespace='cart')),
    url(r'^$', core_views.home, name='home'),
url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
  
     
      url(r'^', include('shop.urls', namespace='shop')),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
