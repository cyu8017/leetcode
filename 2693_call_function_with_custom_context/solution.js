// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

Function.prototype.callPolyfill = function(obj, ...args) {
    const key = Symbol();
    obj[key] = this;
    const res = obj[key](...args);
    delete obj[key];
    return res;
};
