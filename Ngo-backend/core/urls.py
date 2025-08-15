"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root endpoint view
def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "Welcome to the API. Available routes: /api/, /donation/, /admin/"
    })

# Catch-all view for undefined routes (optional but useful for APIs)
def not_found(request, exception=None):
    return JsonResponse({"error": "Endpoint not found"}, status=404)

urlpatterns = [
    path('', home),  # Root path
    path('admin/', admin.site.urls),
    path('api/', include('ngo.urls')),
    path('donation/', include('donation.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
]

# Custom error handlers
handler404 = not_found
