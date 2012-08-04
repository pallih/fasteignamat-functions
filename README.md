fasteignamat-functions
======================

Functions to scrape info on landnr and fastanr from skra.is

Demo.py should return this (when run with the hardcoded fastanr and landnr for Vesturbrún 2, 104 Reykjavík).

The "HEINUM" returned from the geoserver is the identifier that skra.is uses (not landnr or fastanr). To get a aerial image you can for example do this:

http://geo.skra.is/geoserver/vefur/heinum/HEINUM

for this example = http://geo.skra.is/geoserver/vefur/heinum/1018969

Info returned:
--------------

Fastanr - general info for fastanr:  201-9612
Info from: http://skra.is/default.aspx?pageid=1000&streetname=201-9612
   fasteignamat : 18.500.000
   birtst : 75.9 m2
   fastanr : 201-9612
   lodahlmat : 2.560.000
   brunabotamat : 16.500.000
   notkun : Íbúðareign
   byggar : 1957
   fastmat : 16.350.000
   fastanumer_org : 201-9612
   merking : 01 0001
---
Fastanr - extended info for fastanr:  201-9612
Info from: http://skra.is/Pages/957?fastnr=2019612
   Byggingarefni : Steypa
   Fastanumer : 2019612
   Geymsla_ofl : 17,9
   Heiti : Vesturbrún 2 01-0001
   Stada : Fullgert
   Er_lyfta_i_husi : Nei
   Fjoldi_sturta : 1
   Fjoldi_haeda_i_ibud : 1
   Adalhaed_ibudar : 00
   Metid_afskriftarar : 1957
   Fjoldi_klosetta : 1
   Fjoldi_ibuda_i_husi : 3
   Matssvaedi : Laugarneshverfi/Vogar
   Ibud_i_kjallara : 58
   Flokkun : Íbúðareign
   Undirmatssvaedi : Laugarás
   fastanumer_org : 201-9612
---
Fastanr - land info for fastanr:  201-9612
Info from: http://skra.is/default.aspx?pageid=1000&streetname=201-9612
   notkun : Íbúðarhúsalóð
   stadgreinir : 0-1- 1380201
   land : 104739
   fastanumer_org : 201-9612
   staerd : 709.0 m²
---
Landr geocoded - geocoded info for landnr:  104739
   geometry_name : HNIT
   LM_HEIMILISFANG : Vesturbrún 2  (104739)
   ATH : None
   MATSNR : None
   id : VSTADF.fid-38ccc4ad_138f1e66f4c_69f4
   lng : -21.8680851
   SVFNR : 0000
   HEITI_TGF : Vesturbrún
   HUSNR : 2
   POSTNR : 104
   coordinates : [360440, 408034.384090909]
   YFIRF_HEITI : None
   DAGS_LEIDR : 2010-01-04
   TEGHNIT : 0
   HNITNUM : 10012946
   NAKV_XY : None
   HUSMERKING : 2
   type : Point
   HEITI_NF : Vesturbrún
   BOKST : None
   bbox : [360440, 408034.384090909, 360440, 408034.384090909]
   crs_type : EPSG
   lat : 64.1466508
   VEF_BIRTING : Vesturbrún 2  (104739)
   DAGS_INN : 2007-09-07
   GAGNA_EIGN : Fasteignaskrá Íslands
   YFIRFARID : 0
   LANDNR : 104739
   SERHEITI : None
   NOTNR : 956
   HEINUM : 1018969
   crs_properties : {u'code': u'3057'}
   VIDSK : None
---