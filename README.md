About parl_uk
===================

What it does
------------

Loads all the UK Parliamentary constituencies into django via
geodjango. Allows you to do some interesting things with geodata
and parliamentary constituencies.

Requirements
------------
django 1.1
gdal
A spatially aware database (Like Postgresql)

Quickstart
----------
Install django
Install geodjango dependencies
Clone the repro
Add to installed apps `parl_uk`
Run ./manage.py syncdb
Run ./manage.py load_mp_boundaries -f <PATH_TO_FILE>westminster_const_region.shp
Go make Tea / Beverage of choice

What can I do with this?
-----------------------
Any UK geodata (geocoded addresses, etc) can be grouped by constituency. So for example, say you were a uk NGO and wanted to generate a per constituency campaign site for a possible upcoming election, you could easily use this and postcode data to work out which constituency and thus which MP that represents them. You get the idea.









