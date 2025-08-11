from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VolunteerApplicationViewSet
from .views import ContactMessageViewSet

router = DefaultRouter()
router.register(r'volunteers', VolunteerApplicationViewSet)
router.register(r'contact-messages', ContactMessageViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    # Include the router URLs for other apps
    path('', include(router.urls)),
    
    # Add this line to include the donation app's URLs
    path('donation/', include('donation.urls')),
]