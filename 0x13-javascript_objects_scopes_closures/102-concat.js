#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', (error, data) => {
  if (error) {
    console.log('error in reading the file');
  } else {
    fs.appendFile(args[4], data, (err) => {
      if (err) throw err;
    });
  }
});

fs.readFile(args[3], 'utf8', (error, data) => {
  if (error) {
    console.log('error in reading the file');
  } else {
    fs.appendFile(args[4], data, (err) => {
      if (err) throw err;
    });
  }
});
