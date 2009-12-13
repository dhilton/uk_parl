from django.contrib.gis import admin
from models import Constituencies

admin.site.register(Constituencies, admin.GeoModelAdmin)

