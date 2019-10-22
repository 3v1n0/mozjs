// |reftest| skip-if((function(){try{eval('c=class{x;}');return(false);}catch{return(true);}})()) -- class-fields-public is not enabled unconditionally
// This file was procedurally generated from the following sources:
// - src/class-elements/literal-names.case
// - src/class-elements/productions/cls-decl-after-same-line-gen.template
/*---
description: Literal property names (field definitions after a generator in the same line)
esid: prod-FieldDefinition
features: [class-fields-public, generators, class]
flags: [generated]
includes: [propertyHelper.js]
info: |
    ClassElement:
      ...
      FieldDefinition ;

    FieldDefinition:
      ClassElementName Initializer_opt

    ClassElementName:
      PropertyName

---*/
const fn = function() {}



class C {
  *m() { return 42; } a; b = 42;
  c = fn;
  
}

var c = new C();

assert.sameValue(c.m().next().value, 42);
assert.sameValue(Object.hasOwnProperty.call(c, "m"), false);
assert.sameValue(c.m, C.prototype.m);

verifyProperty(C.prototype, "m", {
  enumerable: false,
  configurable: true,
  writable: true,
});

assert.sameValue(Object.hasOwnProperty.call(C.prototype, "a"), false);
assert.sameValue(Object.hasOwnProperty.call(C, "a"), false);

verifyProperty(c, "a", {
  value: undefined,
  enumerable: true,
  writable: true,
  configurable: true
});

assert.sameValue(Object.hasOwnProperty.call(C.prototype, "b"), false);
assert.sameValue(Object.hasOwnProperty.call(C, "b"), false);

verifyProperty(c, "b", {
  value: 42,
  enumerable: true,
  writable: true,
  configurable: true
});

assert.sameValue(Object.hasOwnProperty.call(C.prototype, "c"), false);
assert.sameValue(Object.hasOwnProperty.call(C, "c"), false);

verifyProperty(c, "c", {
  value: fn,
  enumerable: true,
  writable: true,
  configurable: true
});


reportCompare(0, 0);
