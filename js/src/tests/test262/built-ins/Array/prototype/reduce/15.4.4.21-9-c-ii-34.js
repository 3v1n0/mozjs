// Copyright (c) 2012 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
esid: sec-array.prototype.reduce
es5id: 15.4.4.21-9-c-ii-34
description: Array.prototype.reduce - Error object can be used as accumulator
---*/

var objError = new RangeError();

var accessed = false;

function callbackfn(prevVal, curVal, idx, obj) {
  accessed = true;
  return prevVal === objError;
}

var obj = {
  0: 11,
  length: 1
};

assert.sameValue(Array.prototype.reduce.call(obj, callbackfn, objError), true, 'Array.prototype.reduce.call(obj, callbackfn, objError)');
assert(accessed, 'accessed !== true');

reportCompare(0, 0);
