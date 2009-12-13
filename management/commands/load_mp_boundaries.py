import os
from django.contrib.gis.utils import LayerMapping
from uk_parl.models import Constituencies
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option


con_mapping = {
    'name' : 'NAME',
    'area_code' : 'AREA_CODE',
    'descriptio' : 'DESCRIPTIO',
    'file_name' : 'FILE_NAME',
    'number' : 'NUMBER',
    'number0' : 'NUMBER0',
    'polygon_id' : 'POLYGON_ID',
    'unit_id' : 'UNIT_ID',
    'code' : 'CODE',
    'hectares' : 'HECTARES',
    'area' : 'AREA',
    'type_code' : 'TYPE_CODE',
    'descript0' : 'DESCRIPT0',
    'type_cod0' : 'TYPE_COD0',
    'descript1' : 'DESCRIPT1',
    'geom' : 'POLYGON',
}


class Command(BaseCommand):
	"""
	Loads the data from the ESRI .shp file into the database.
	"""
	option_list = BaseCommand.option_list + (
        	make_option('--file-path', '-f', dest='file',
            		help='Path to the .shp file'),
    	)
    	help = 'Loads the OS data westminster constituencies shapefile into the database.'

    	def handle(self,file, **options):
		lm = LayerMapping(Constituencies, file,con_mapping, transform=False)
		lm.save(strict=True)





