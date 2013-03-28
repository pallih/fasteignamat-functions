fasteignamat.js
===============

This is an experimental Node.js rewrite.  Outputs are slightly different (javascript objects) and are retrieved asynchronously via standard (err,data) callback functions.

Dependencies: [`request`](https://github.com/mikeal/request) and [`cheerio`](https://github.com/MatthewMueller/cheerio) are registered in the `package.json` and can be installed automatically  using the Node Package Manager:

```
npm install
```

A command line interface is provided in addition to the module.exports:
```
node fasteignamat.js [numer]
```
If numer is not provided a default identifier is used.