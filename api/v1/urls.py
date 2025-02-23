from django.urls import path, include

urlpatterns = [
    path('main/', include('api.v1.main.urls')),
]
