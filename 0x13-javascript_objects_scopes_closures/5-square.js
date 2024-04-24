#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (h) {
    super(h, h);
  }

  charPrint () {
    if (this.h === undefined) {
      super.print();
    }
  }
}
module.exports = Square;
