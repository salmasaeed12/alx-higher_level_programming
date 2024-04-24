#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (h) {
    super(h, h);
  }

  charPrint (char) {
    if (char === undefined) {
      super.print();
    } else {
      let i = 0;
    let j = 0;
    let wide = '';
    while (i < this.width) {
      wide += 'C';
      i++;
    }

    while (j < this.height) {
      console.log(wide);
      j++;
    }
    }

  }

}

module.exports = Square;
