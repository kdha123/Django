from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('polls/', include('polls.urls'))
]
