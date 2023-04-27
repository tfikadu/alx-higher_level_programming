#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.alx-tools.com/api/films/:id'.concat(process.argv[2]);

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
