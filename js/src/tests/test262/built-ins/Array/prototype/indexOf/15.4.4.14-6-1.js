// Copyright (c) 2012 Ecma International.  All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
esid: sec-array.prototype.indexof
es5id: 15.4.4.14-6-1
description: >
    Array.prototype.indexOf returns -1 if fromIndex is greater than
    Array length
---*/

var a = [1, 2, 3];

assert.sameValue(a.indexOf(1, 5), -1, 'a.indexOf(1,5)');
assert.sameValue(a.indexOf(1, 3), -1, 'a.indexOf(1,3)');
assert.sameValue([].indexOf(1, 0), -1, '[ ].indexOf(1,0)');

reportCompare(0, 0);
