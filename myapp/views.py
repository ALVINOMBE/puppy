from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from myapp.models import Breed, Dog, HealthRecord, Owner, Veterinarian

class BreedListView(ListView):
    model = Breed
    template_name = 'breed_list.html'
    context_object_name = 'breeds'

class DogListView(ListView):
    model = Dog
    template_name = 'dog_list.html'
    context_object_name = 'dogs'

class HealthRecordListView(ListView):
    model = HealthRecord
    template_name = 'health_record_list.html'
    context_object_name = 'health_records'

class OwnerListView(ListView):
    model = Owner
    template_name = 'owner_list.html'
    context_object_name = 'owners'

class VeterinarianListView(ListView):
    model = Veterinarian
    template_name = 'veterinarian_list.html'
    context_object_name = 'veterinarians'


def home(request):
    return render(request, 'base.html')