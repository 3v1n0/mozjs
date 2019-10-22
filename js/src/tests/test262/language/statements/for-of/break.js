// Copyright (C) 2013 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.
/*---
es6id: 13.6.4.13 S5.n
description: >
    Control flow during body evaluation should honor `break` statements.
features: [generators]
---*/

function* values() {
  yield 1;
  $ERROR('This code is unreachable (following `yield` statement).');
}
var iterator = values();
var i = 0;

for (var x of iterator) {
  i++;
  break;

  $ERROR('This code is unreachable.');
}

assert.sameValue(i, 1);

reportCompare(0, 0);
