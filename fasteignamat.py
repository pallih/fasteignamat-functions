# -*- coding: utf-8 -*-

#Fasteignamat.py - functions for scraping info from Fasteignamat Íslands (www.skra.is)
#For fastanr.:
#   Returns general info
#   Return extended info
#   Returns land info and landnr
#For landnr.:
#   Return geo info from skra.is geoserver + ISN93 xx,yy converted to WGS84 lat/lng
#Author: pallih@gogn.in / @pallih
#See demo.py for demo usage


import requests
from random import choice
import string
import lxml.html
import json
import math

chars = string.letters + string.digits
random =  ''.join([choice(chars) for i in xrange(4)]) # create a random string for url appending to avoid cache


def latin1_to_ascii (unicrap):
    """This takes a UNICODE string and replaces Latin-1 characters with
        something equivalent in 7-bit ASCII. It returns a plain ASCII string.
        This function makes a best effort to convert Latin-1 characters into
        ASCII equivalents. It does not just strip out the Latin-1 characters.
        All characters in the standard 7-bit ASCII range are preserved.
        In the 8th bit range all the Latin-1 accented letters are converted
        to unaccented equivalents. Most symbol characters are converted to
        something meaningful. Anything not converted is deleted.
    """
    xlate={u'\N{ACUTE ACCENT}': "'",
 u'\N{BROKEN BAR}': '|',
 u'\N{CEDILLA}': '{cedilla}',
 u'\N{CENT SIGN}': '{cent}',
 u'\N{COPYRIGHT SIGN}': '{C}',
 u'\N{CURRENCY SIGN}': '{currency}',
 u'\N{DEGREE SIGN}': '{degrees}',
 u'\N{DIAERESIS}': '{umlaut}',
 u'\N{DIVISION SIGN}': '/',
 u'\N{FEMININE ORDINAL INDICATOR}': '{^a}',
 u'\N{INVERTED EXCLAMATION MARK}': '!',
 u'\N{INVERTED QUESTION MARK}': '?',
 u'\N{LATIN CAPITAL LETTER A WITH ACUTE}': 'A',
 u'\N{LATIN CAPITAL LETTER A WITH CIRCUMFLEX}': 'A',
 u'\N{LATIN CAPITAL LETTER A WITH DIAERESIS}': 'A',
 u'\N{LATIN CAPITAL LETTER A WITH GRAVE}': 'A',
 u'\N{LATIN CAPITAL LETTER A WITH RING ABOVE}': 'A',
 u'\N{LATIN CAPITAL LETTER A WITH TILDE}': 'A',
 u'\N{LATIN CAPITAL LETTER AE}': 'Ae',
 u'\N{LATIN CAPITAL LETTER C WITH CEDILLA}': 'C',
 u'\N{LATIN CAPITAL LETTER E WITH ACUTE}': 'E',
 u'\N{LATIN CAPITAL LETTER E WITH CIRCUMFLEX}': 'E',
 u'\N{LATIN CAPITAL LETTER E WITH DIAERESIS}': 'E',
 u'\N{LATIN CAPITAL LETTER E WITH GRAVE}': 'E',
 u'\N{LATIN CAPITAL LETTER ETH}': 'D',
 u'\N{LATIN CAPITAL LETTER I WITH ACUTE}': 'I',
 u'\N{LATIN CAPITAL LETTER I WITH CIRCUMFLEX}': 'I',
 u'\N{LATIN CAPITAL LETTER I WITH DIAERESIS}': 'I',
 u'\N{LATIN CAPITAL LETTER I WITH GRAVE}': 'I',
 u'\N{LATIN CAPITAL LETTER N WITH TILDE}': 'N',
 u'\N{LATIN CAPITAL LETTER O WITH ACUTE}': 'O',
 u'\N{LATIN CAPITAL LETTER O WITH CIRCUMFLEX}': 'O',
 u'\N{LATIN CAPITAL LETTER O WITH DIAERESIS}': 'O',
 u'\N{LATIN CAPITAL LETTER O WITH GRAVE}': 'O',
 u'\N{LATIN CAPITAL LETTER O WITH STROKE}': 'O',
 u'\N{LATIN CAPITAL LETTER O WITH TILDE}': 'O',
 u'\N{LATIN CAPITAL LETTER THORN}': 'th',
 u'\N{LATIN CAPITAL LETTER U WITH ACUTE}': 'U',
 u'\N{LATIN CAPITAL LETTER U WITH CIRCUMFLEX}': 'U',
 u'\N{LATIN CAPITAL LETTER U WITH DIAERESIS}': 'U',
 u'\N{LATIN CAPITAL LETTER U WITH GRAVE}': 'U',
 u'\N{LATIN CAPITAL LETTER Y WITH ACUTE}': 'Y',
 u'\N{LATIN SMALL LETTER A WITH ACUTE}': 'a',
 u'\N{LATIN SMALL LETTER A WITH CIRCUMFLEX}': 'a',
 u'\N{LATIN SMALL LETTER A WITH DIAERESIS}': 'a',
 u'\N{LATIN SMALL LETTER A WITH GRAVE}': 'a',
 u'\N{LATIN SMALL LETTER A WITH RING ABOVE}': 'a',
 u'\N{LATIN SMALL LETTER A WITH TILDE}': 'a',
 u'\N{LATIN SMALL LETTER AE}': 'ae',
 u'\N{LATIN SMALL LETTER C WITH CEDILLA}': 'c',
 u'\N{LATIN SMALL LETTER E WITH ACUTE}': 'e',
 u'\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}': 'e',
 u'\N{LATIN SMALL LETTER E WITH DIAERESIS}': 'e',
 u'\N{LATIN SMALL LETTER E WITH GRAVE}': 'e',
 u'\N{LATIN SMALL LETTER ETH}': 'd',
u'\N{LATIN SMALL LETTER I WITH ACUTE}': 'i',
 u'\N{LATIN SMALL LETTER I WITH CIRCUMFLEX}': 'i',
 u'\N{LATIN SMALL LETTER I WITH DIAERESIS}': 'i',
 u'\N{LATIN SMALL LETTER I WITH GRAVE}': 'i',
 u'\N{LATIN SMALL LETTER N WITH TILDE}': 'n',
 u'\N{LATIN SMALL LETTER O WITH ACUTE}': 'o',
 u'\N{LATIN SMALL LETTER O WITH CIRCUMFLEX}': 'o',
 u'\N{LATIN SMALL LETTER O WITH DIAERESIS}': 'o',
 u'\N{LATIN SMALL LETTER O WITH GRAVE}': 'o',
 u'\N{LATIN SMALL LETTER O WITH STROKE}': 'o',
 u'\N{LATIN SMALL LETTER O WITH TILDE}': 'o',
 u'\N{LATIN SMALL LETTER SHARP S}': 'ss',
 u'\N{LATIN SMALL LETTER THORN}': 'th',
 u'\N{LATIN SMALL LETTER U WITH ACUTE}': 'u',
 u'\N{LATIN SMALL LETTER U WITH CIRCUMFLEX}': 'u',
 u'\N{LATIN SMALL LETTER U WITH DIAERESIS}': 'u',
 u'\N{LATIN SMALL LETTER U WITH GRAVE}': 'u',
 u'\N{LATIN SMALL LETTER Y WITH ACUTE}': 'y',
 u'\N{LATIN SMALL LETTER Y WITH DIAERESIS}': 'y',
 u'\N{LEFT-POINTING DOUBLE ANGLE QUOTATION MARK}': '&lt;&lt;',
 u'\N{MACRON}': '_',
 u'\N{MASCULINE ORDINAL INDICATOR}': '{^o}',
 u'\N{MICRO SIGN}': '{micro}',
 u'\N{MIDDLE DOT}': '*',
 u'\N{MULTIPLICATION SIGN}': '*',
 u'\N{NOT SIGN}': '{not}',
 u'\N{PILCROW SIGN}': '{paragraph}',
 u'\N{PLUS-MINUS SIGN}': '{+/-}',
 u'\N{POUND SIGN}': '{pound}',
 u'\N{REGISTERED SIGN}': '{R}',
 u'\N{RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK}': '&gt;&gt;',
 u'\N{SECTION SIGN}': '{section}',
 u'\N{SOFT HYPHEN}': '-',
 u'\N{SUPERSCRIPT ONE}': '{^1}',
 u'\N{SUPERSCRIPT THREE}': '{^3}',
 u'\N{SUPERSCRIPT TWO}': '{^2}',
 u'\N{VULGAR FRACTION ONE HALF}': '{1/2}',
 u'\N{VULGAR FRACTION ONE QUARTER}': '{1/4}',
 u'\N{VULGAR FRACTION THREE QUARTERS}': '{3/4}',
 u'\N{YEN SIGN}': '{yen}',
 u'\N{LEFT PARENTHESIS}': '', #Paranthesis to nothing
 u'\N{RIGHT PARENTHESIS}': '',
 u'\N{QUESTION MARK}': '', #Question mark strip
 u'\N{FULL STOP}': '', #period strip
 u'\N{COMMA}': '_', #comma to underscore
u'\N{SPACE}': '_' #convert space to underscore
        }

    r = ''
    for i in unicrap:
        if xlate.has_key(i):
            r += xlate[i]
        elif ord(i) >= 0x80:
            pass
        else:
            r += str(i)
    return r

def fastanr_extended_info(fastanr):
    url = 'http://www.skra.is/default.aspx?pageid=957' + "&x=" + str(random) #append a random string to url to avoid bad status line / cache ...
    params = {'pageid':'957', 'fnum':str(fastanr.replace('-',''))}
    r = requests.post(url,data=params)
    html = r.content
    root = lxml.html.fromstring(html)
    xpath = '//table[@class="matsforsendur"]/tr/.'
    table = root.xpath(xpath)
    record = {}
    record['fastanumer_org'] = fastanr
    for tr in table:
        if tr[0].tag == 'th' and tr[0].attrib != {'colspan': '2', 'style': 'text-align: center;'}:
            record[latin1_to_ascii(tr[0].text)] = tr[1].text
    return record

def fastanr_general_info(fastanr):
    url = 'http://www.skra.is/default.aspx?pageid=1000' + "&x=" + str(random) #append a random string to url to avoid bad status line / cache ...
    params = {'pageid':'1000', 'streetname':str(fastanr.replace('-',''))}
    r = requests.post(url,data=params)
    html = r.content
    root = lxml.html.fromstring(html)
    xpath = '//table[@class="resulttable large"]//tbody/tr/.' #taflan med nidurstodum
    table = root.xpath(xpath)
    record = {}
    record['fastanumer_org'] = fastanr
    for tr in table:
        try:
            if tr[0][0][2].text is not None:
                if tr[0][0][2].text == fastanr:
                    for td in tr:
                        if td.attrib['header'] == 'fastmat' or td.attrib['header'] == 'fasteignamat':
                            record[td.attrib['header']] = td.text_content().strip()
                        elif td.attrib['header'] == 'fastanr':
                            record[td.attrib['header']] = td[0][2].text_content().strip()
                        else:
                            record[td.attrib['header']] = td.text.strip()
        except:
            if tr[0].text == fastanr:
                for td in tr:
                    if td.attrib['header'] == 'fastmat' or td.attrib['header'] == 'fasteignamat':
                        record[td.attrib['header']] = td.text_content().strip()
                    else:
                        record[td.attrib['header']] = td.text.strip()
    return record

def fastanr_land_info(fastanr):

    url = 'http://www.skra.is/default.aspx?pageid=1000'
    params = {'pageid':'1000', 'streetname':str(fastanr.replace('-',''))}
    r = requests.post(url,data=params)
    html = r.content
    root = lxml.html.fromstring(html)
    xpath = '//table[@class="resulttable small"]//tbody/tr/.' #taflan med nidurstodum
    table = root.xpath(xpath)
    record = {}
    record['fastanumer_org'] = fastanr
    if table != []:
        for tr in table:
            for td in tr:
                record[td.attrib['header']] = td.text.strip()
    else:
        record['landnr_lookup_error'] = 1
    return record

def isnet93_to_wgs84(xx,yy):
    x = xx;
    y = yy;
    a = 6378137.0;
    f = 1/298.257222101;
    lat1 = 64.25;
    lat2 = 65.75;
    latc = 65.00;
    lonc = 19.00;
    eps = 0.00000000001;
    def fx(p):
        return  a * math.cos(p/rho)/math.sqrt(1 - math.pow(e*math.sin(p/rho),2));
    def f1(p):
        return math.log( (1 - p)/(1 + p) )
    def f2(p):
        return f1(p) - e * f1(e * p)
    def f3(p):
        return pol1*math.exp( (f2(math.sin(p/rho)) - f2sin1)*sint/2)
    rho = 45/math.atan2(1.0,1.0)
    e = math.sqrt(f * (2 - f))
    dum = f2(math.sin(lat1/rho)) - f2(math.sin(lat2/rho))
    sint = 2 * ( math.log(fx(lat1)) - math.log(fx(lat2)) ) / dum
    f2sin1 = f2(math.sin(lat1/rho))
    pol1 = fx(lat1)/sint
    polc = f3(latc) + 500000.0
    peq = a * math.cos(latc/rho)/(sint*math.exp(sint*math.log((45-latc/2)/rho)))
    pol = math.sqrt( math.pow(x-500000,2) + math.pow(polc-y,2))
    lat = 90 - 2 * rho * math.atan( math.exp( math.log( pol / peq ) / sint ) )
    lon = 0
    fact = rho * math.cos(lat / rho) / sint / pol
    fact = rho * math.cos(lat / rho) / sint / pol
    delta = 1.0
    while( math.fabs(delta) > eps ):
        delta = ( f3(lat) - pol ) * fact
        lat += delta
    lon = -(lonc + rho * math.atan( (500000 - x) / (polc - y) ) / sint)

    #return round(lat,5), round(lon,5)
    latlon = {}
    latlon['lat'] = round(lat,7)
    latlon['lng'] = round(lon,7)
    return latlon

def geocode_landnr(landnr):
    url = 'http://geo.skra.is/geoserver/wfs'
    params = {
    'service':'wfs',
    'version':'1.1.0',
    'request':'GetFeature',
    'typename':'fasteignaskra:VSTADF',
    'outputformat':'json',
    #'maxfeatures':'5',
    'filter':'<Filter><PropertyIsLike wildCard="*" singleChar="#" escapeChar="!"><PropertyName>fasteignaskra:LANDNR</PropertyName><Literal>%s</Literal></PropertyIsLike></Filter>' % (landnr)
    }
    r = requests.post(url,data=params)
    jsonstring = r.content
    process = json.loads(jsonstring)
    record = {}
    try:
        for p in process['features']:
            for key, value in dict.items(p['properties']):
                record[key] =  value
            for key, value in dict.items(p['geometry']):
                record[key] =  value
            record['id'] = p['id']
            record['geometry_name'] = p['geometry_name']
    except:
        pass
    try:
        record['crs_type'] =  process['crs']['type']
    except:
        pass
    try:
        record['crs_properties'] =  process['crs']['properties']
    except:
        pass
    try:
        record['bbox'] =  process['bbox']
    except:
        pass
    latlng = isnet93_to_wgs84(record['coordinates'][0],record['coordinates'][1])
    record['lat'] = latlng['lat']
    record['lng'] = latlng['lng']
    return record
    return record



