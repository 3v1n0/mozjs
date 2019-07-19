// Copyright (c) 2012 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
esid: sec-array.prototype.indexof
es5id: 15.4.4.14-8-3
description: >
    Array.prototype.indexOf returns -1 when abs('fromIndex') is length
    of array - 1
---*/

assert.sameValue([1, 2, 3, 4].indexOf(1, -3), -1, '[1, 2, 3, 4].indexOf(1, -3)');

reportCompare(0, 0);
