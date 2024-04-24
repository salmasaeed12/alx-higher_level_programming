#!/usr/bin/node

const mylist = require('./100-data').list;

console.log(mylist);
console.log(mylist.map((item, index) => { return item * index; }));
// map here is an itarator that itarates over the list, and the
// first argument is first item of the list, second argument is its index and
// the right side is the oparation that will be done on each item of the list
