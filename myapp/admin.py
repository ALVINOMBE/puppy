from django.contrib import admin

# Register your models here.
from .models import BaseModel, Breed, Dog, HealthRecord, Owner, Veterinarian

admin.site.register(Breed)
admin.site.register(Dog)
admin.site.register(HealthRecord)
admin.site.register(Owner)
admin.site.register(Veterinarian)

