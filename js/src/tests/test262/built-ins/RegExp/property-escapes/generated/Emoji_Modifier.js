// |reftest| skip -- regexp-unicode-property-escapes is not supported
// Copyright 2019 Mathias Bynens. All rights reserved.
// This code is governed by the BSD license found in the LICENSE file.

/*---
author: Mathias Bynens
description: >
  Unicode property escapes for `Emoji_Modifier`
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
    [0x01F3FB, 0x01F3FF]
  ]
});
testPropertyEscapes(
  /^\p{Emoji_Modifier}+$/u,
  matchSymbols,
  "\\p{Emoji_Modifier}"
);

const nonMatchSymbols = buildString({
  loneCodePoints: [],
  ranges: [
    [0x00DC00, 0x00DFFF],
    [0x000000, 0x00DBFF],
    [0x00E000, 0x01F3FA],
    [0x01F400, 0x10FFFF]
  ]
});
testPropertyEscapes(
  /^\P{Emoji_Modifier}+$/u,
  nonMatchSymbols,
  "\\P{Emoji_Modifier}"
);

reportCompare(0, 0);
