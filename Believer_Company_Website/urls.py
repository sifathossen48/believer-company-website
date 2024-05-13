from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home_Page.urls')),
    path('news/',include('News_Page.urls')),
    path('get_quote/',include('Get_Quote_Page.urls')),
    path('contact/',include('Contact_Page.urls'))
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

