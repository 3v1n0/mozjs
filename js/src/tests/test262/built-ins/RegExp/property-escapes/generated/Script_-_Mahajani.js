// |reftest| skip -- regexp-unicode-property-escapes is not supported
// Copyright 2019 Mathias Bynens. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
author: Mathias Bynens
description: >
  Unicode property escapes for `Script=Mahajani`
info: |
  Generated by https://github.com/mathiasbynens/unicode-property-escapes-tests
  Unicode v12.0.0
esid: sec-static-semantics-unicodematchproperty-p
features: [regexp-unicode-property-escapes]
includes: [regExpUtils.js]
---*/

const matchSymbols = buildString({
  loneCodePoints: [],
  ranges: [
    [0x011150, 0x011176]
  ]
});
testPropertyEscapes(
  /^\p{Script=Mahajani}+$/u,
  matchSymbols,
  "\\p{Script=Mahajani}"
);
testPropertyEscapes(
  /^\p{Script=Mahj}+$/u,
  matchSymbols,
  "\\p{Script=Mahj}"
);
testPropertyEscapes(
  /^\p{sc=Mahajani}+$/u,
  matchSymbols,
  "\\p{sc=Mahajani}"
);
testPropertyEscapes(
  /^\p{sc=Mahj}+$/u,
  matchSymbols,
  "\\p{sc=Mahj}"
);

const nonMatchSymbols = buildString({
  loneCodePoints: [],
  ranges: [
    [0x00DC00, 0x00DFFF],
    [0x000000, 0x00DBFF],
    [0x00E000, 0x01114F],
    [0x011177, 0x10FFFF]
  ]
});
testPropertyEscapes(
  /^\P{Script=Mahajani}+$/u,
  nonMatchSymbols,
  "\\P{Script=Mahajani}"
);
testPropertyEscapes(
  /^\P{Script=Mahj}+$/u,
  nonMatchSymbols,
  "\\P{Script=Mahj}"
);
testPropertyEscapes(
  /^\P{sc=Mahajani}+$/u,
  nonMatchSymbols,
  "\\P{sc=Mahajani}"
);
testPropertyEscapes(
  /^\P{sc=Mahj}+$/u,
  nonMatchSymbols,
  "\\P{sc=Mahj}"
);

reportCompare(0, 0);
