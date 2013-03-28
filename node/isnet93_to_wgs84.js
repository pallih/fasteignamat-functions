// Refactoring of https://gist.github.com/avar/585850
function isnet93_to_wgs84(xx, yy) {
  function fx(p) { return  a * Math.cos(p/rho)/Math.sqrt(1 - Math.pow(e*Math.sin(p/rho),2)); }
  function f1(p) { return Math.log( (1 - p)/(1 + p) ); }
  function f2(p) { return f1(p) - e * f1(e * p); }
  function f3(p) { return pol1*Math.exp( (f2(Math.sin(p/rho)) - f2sin1)*sint/2); }

  var x = xx,
      y = yy,
      a = 6378137.0,
      f = 1/298.257222101,
      lat1 = 64.25,
      lat2 = 65.75,
      latc = 65.00,
      lonc = 19.00,
      eps = 0.00000000001,
      rho = 45/Math.atan2(1.0,1.0),
      e = Math.sqrt(f * (2 - f)),
      dum = f2(Math.sin(lat1/rho)) - f2(Math.sin(lat2/rho)),
      sint = 2 * ( Math.log(fx(lat1)) - Math.log(fx(lat2)) ) / dum,
      f2sin1 = f2(Math.sin(lat1/rho)),
      pol1 = fx(lat1)/sint,
      polc = f3(latc) + 500000.0,
      peq = a * Math.cos(latc/rho)/(sint*Math.exp(sint*Math.log((45-latc/2)/rho))),
      pol = Math.sqrt( Math.pow(x-500000,2) + Math.pow(polc-y,2)),
      lat = 90 - 2 * rho * Math.atan( Math.exp( Math.log( pol / peq ) / sint ) ),
      lon = 0,
      fact = rho * Math.cos(lat / rho) / sint / pol,
      delta = 1.0;

  while( Math.abs(delta) > eps ) {
    delta = ( f3(lat) - pol ) * fact;
    lat += delta;
  }

  lon = -(lonc + rho * Math.atan( (500000 - x) / (polc - y) ) / sint);
  return {lat:lat,lon:lon};
}

module.exports = isnet93_to_wgs84;

if (require.main === module)
  console.log(isnet93_to_wgs84(357954,404213));
