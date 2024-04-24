#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let i = 0;
      let j = 0;
      let wide = '';
      while (i < this.width) {
        wide += 'X';
        i++;
      }
  
      while (j < this.height) {
        console.log(wide);
        j++;
      }
    }
  
    rotate () {
      let temp = 0;
      temp = this.height;
      this.height = this.width;
      this.width = temp;
    }
  
    double () {
      this.height *= 2;
      this.width *= 2;
    }
  }
  
  module.exports = Rectangle;
