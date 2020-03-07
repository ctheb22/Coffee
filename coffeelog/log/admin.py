from django.contrib import admin

from .models import Coffee
from .models import Roast
from .models import RoastDataPoints
from .models import RoastLevel

admin.site.register(Coffee)
admin.site.register(Roast)
admin.site.register(RoastDataPoints)
admin.site.register(RoastLevel)