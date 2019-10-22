// |reftest| skip error:SyntaxError -- regexp-named-groups is not supported
// Copyright 2017 the V8 project authors. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
description: GroupSpecifier must be identifier-like.
esid: prod-GroupSpecifier
negative:
  phase: parse
  type: SyntaxError
features: [regexp-named-groups]
---*/

$DONOTEVALUATE();

/(?<𐒤>a)/u;
