from django.urls import path
from .views import BreedListView, DogListView, HealthRecordListView, OwnerListView, VeterinarianListView

urlpatterns = [
    path('breeds/', BreedListView.as_view(), name='breed-list'),
    path('dogs/', DogListView.as_view(), name='dog-list'),
    path('healthrecords/', HealthRecordListView.as_view(), name='healthrecord-list'),
    path('owners/', OwnerListView.as_view(), name='owner-list'),
    path('veterinarians/', VeterinarianListView.as_view(), name='veterinarian-list'),
    # Add more paths as needed for additional views
]
