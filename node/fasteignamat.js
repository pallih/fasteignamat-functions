var request = require("request"),
    cheerio = require("cheerio"),
    isn2wgs = require('isn2wgs');

function general_info(fastanr,callback) {
  if (fastanr[3] && fastanr[3] !=='-') fastanr = fastanr.slice(0,3)+'-'+fastanr.slice(3);
  var url = "http://skra.is/default.aspx?pageid=1000&streetname="+fastanr;
  request(url,function(err,res,body) {
    if (err) return callback(err);
    try {
      var $ = cheerio.load(body),
          ret = {hus:{},land:{}};

      // Parse house/apartment
      var next = $('td:contains("'+fastanr+'")');

      while ( next != (next = next.next())) {
        var text = next.text()
          .replace(/\r/g,"")
          .replace(/\n/g,"")
          .trim();
        ret.hus[next.attr("header")] = text;
      }

      var th = $(".resulttable.small th"),
          td = $(".resulttable.small td");

      // Parse land
      th.each(function(i) {
        ret.land[$(this).text()] = $(td[i]).text().trim();
      });

      callback(!Object.keys(ret.hus).length && !Object.keys(ret.land).length && "not found",ret);
    } catch(e) { callback(e); }
  });
}

function extended_info(fastanr,callback) {
  if (fastanr[3] && fastanr[3] !=='-') fastanr = fastanr.slice(0,3)+'-'+fastanr.slice(3);
  var url = 'http://www.skra.is/default.aspx?pageid=957&fnum='+fastanr.replace("-","");
  request.post(url,function(err,res,body) {
    if (err) return callback(err);
    try {
      var $ = cheerio.load(body),
          ret = {};

      $("th").each(function() {
        if (this.next) {
          ret[$(this).text()] = $(this).next().text();
        }
      });
      callback(!Object.keys(ret).length && "Not Found",ret);
    } catch(e) { callback(e); }
  });
}

function geocode(landnr,callback) {
  var req = {
    url : "http://geo.skra.is/geoserver/wfs",
    method: "POST",
    form : {
      'service':'wfs',
      'version':'1.1.0',
      'request':'GetFeature',
      'typename':'fasteignaskra:VSTADF',
      'outputformat':'json',
      'filter':'<Filter><PropertyIsLike wildCard="*" singleChar="#" escapeChar="!"><PropertyName>fasteignaskra:LANDNR</PropertyName><Literal>'+landnr+'</Literal></PropertyIsLike></Filter>'
    }
  };
  request(req,function(err,res,body) {
    if (err) return callback(err);
    try {
      var ret = {};
      body = JSON.parse(body);
      ret.center = isn2wgs(this,body.features[0].geometry.coordinates);
      ret.bbox = [
        isn2wgs(body.bbox[0],body.bbox[1]),
        isn2wgs(body.bbox[2],body.bbox[3])
      ];
      ret.properties = body.features[0].properties;
      callback(null,ret);
    } catch(e) { callback(e); }
  });
}

module.exports.extended_info = extended_info;
module.exports.general_info = general_info;
module.exports.geocode = geocode;

if (require.main === module) {
  var fnr = process.argv[2];
  if (fnr == '-h' || fnr == '--help') return console.log("Usage: node fasteignamat.js [fasteignanumer]");
  fnr = fnr  || "201-9612";
  extended_info(fnr,console.log);
  general_info(fnr,function(err,d) {
    if (err) return console.log(err);
    console.log(d);
    geocode(d.land.Land,console.log);
  });
}