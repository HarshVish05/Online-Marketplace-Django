from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("", include('core.urls')),  # first it will loop through all of the parts here i.e from core.urls and then will look into the next part
    path('items/', include('item.urls')),    # all urls beggining with items will automatically go into item.urls
    path('dashboard/', include('dashboard.urls')),
    path('conversation/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # this static part is added to check the images dont do this in production
