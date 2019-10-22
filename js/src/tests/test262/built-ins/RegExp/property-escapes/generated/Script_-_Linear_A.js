// |reftest| skip -- regexp-unicode-property-escapes is not supported
// Copyright 2019 Mathias Bynens. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
author: Mathias Bynens
description: >
  Unicode property escapes for `Script=Linear_A`
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
    [0x010600, 0x010736],
    [0x010740, 0x010755],
    [0x010760, 0x010767]
  ]
});
testPropertyEscapes(
  /^\p{Script=Linear_A}+$/u,
  matchSymbols,
  "\\p{Script=Linear_A}"
);
testPropertyEscapes(
  /^\p{Script=Lina}+$/u,
  matchSymbols,
  "\\p{Script=Lina}"
);
testPropertyEscapes(
  /^\p{sc=Linear_A}+$/u,
  matchSymbols,
  "\\p{sc=Linear_A}"
);
testPropertyEscapes(
  /^\p{sc=Lina}+$/u,
  matchSymbols,
  "\\p{sc=Lina}"
);

const nonMatchSymbols = buildString({
  loneCodePoints: [],
  ranges: [
    [0x00DC00, 0x00DFFF],
    [0x000000, 0x00DBFF],
    [0x00E000, 0x0105FF],
    [0x010737, 0x01073F],
    [0x010756, 0x01075F],
    [0x010768, 0x10FFFF]
  ]
});
testPropertyEscapes(
  /^\P{Script=Linear_A}+$/u,
  nonMatchSymbols,
  "\\P{Script=Linear_A}"
);
testPropertyEscapes(
  /^\P{Script=Lina}+$/u,
  nonMatchSymbols,
  "\\P{Script=Lina}"
);
testPropertyEscapes(
  /^\P{sc=Linear_A}+$/u,
  nonMatchSymbols,
  "\\P{sc=Linear_A}"
);
testPropertyEscapes(
  /^\P{sc=Lina}+$/u,
  nonMatchSymbols,
  "\\P{sc=Lina}"
);

reportCompare(0, 0);
