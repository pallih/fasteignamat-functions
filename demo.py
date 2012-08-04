
# -*- coding: utf-8 -*-
import fasteignamat


## DEMO
test_fastanr = '201-9612' # Vesturbrún 2
test_landnr = '104739' # Vesturbrún 2

print 'Fastanr - general info for fastanr: ', test_fastanr
print 'Info from: http://skra.is/default.aspx?pageid=1000&streetname=201-9612'
for k,v in fasteignamat.fastanr_general_info(test_fastanr).items():
    print '  ',k,":",v
print '---'

print 'Fastanr - extended info for fastanr: ', test_fastanr
print 'Info from: http://skra.is/Pages/957?fastnr=2019612'
for k,v in fasteignamat.fastanr_extended_info(test_fastanr).items():
    print '  ',k,':',v
print '---'

print 'Fastanr - land info for fastanr: ', test_fastanr
print 'Info from: http://skra.is/default.aspx?pageid=1000&streetname=201-9612'
for k,v in fasteignamat.fastanr_land_info(test_fastanr).items():
    print '  ',k,':',v
print '---'

print 'Landr geocoded - geocoded info for landnr: ', test_landnr
for k,v in fasteignamat.geocode_landnr(test_landnr).items():
    print '  ',k,':',v
print '---'