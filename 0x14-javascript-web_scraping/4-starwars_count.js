#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (let result = 0; result < films.length; result++) {
      const characters = films[result].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.alx-tools.com/api/films/' || characters[j] === 'http://swapi-api.alx.io/api/people/18/') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
