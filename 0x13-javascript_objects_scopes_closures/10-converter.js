#!/usr/bin/node

exports.converter = function (base) {
    function display (num) {
      return num.toString(base); // convert the number to specific base passed to it
    }
    return display;
  };
