// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

var curry = function(fn) {
    return function curried(...args) {
        if (args.length >= fn.length) return fn(...args);
        return function(...next) {
            return curried(...args, ...next);
        };
    };
};
