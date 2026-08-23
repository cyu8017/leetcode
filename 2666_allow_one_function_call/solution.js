// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

var once = function(fn) {
    let called = false;
    let res;
    return function(...args) {
        if (called) return undefined;
        called = true;
        res = fn(...args);
        return res;
    };
};
