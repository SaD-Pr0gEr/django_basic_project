from django.urls import path, include

urlpatterns = [
    path('main/', include('apps.api.v1.main.urls')),
]
