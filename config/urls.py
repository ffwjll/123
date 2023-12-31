from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_like
from core.views import reg_form, magic_number
from play_list.views import play_list, add_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reg_form),
    path('magic_number/', magic_number),
    path('post_list/', post_list, name='post_list'),
    path('play_list/', play_list),
    path('add_video/', add_video),
    path('post_like/', post_like, name='post_like'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
