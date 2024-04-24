#!/usr/bin/node
exports.esrever = function (list) {
    const myList = [];
    let i = 0;
    let j = 0;
  
    while (list[i] !== undefined) {
      i++;
    }
  
    while (i--) {
      myList[j] = list[i];
      j++;
    }
    return myList;
  };
