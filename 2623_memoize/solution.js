// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

var memoize = function(fn) {
    const cache = new Map();
    return function(x) {
        if (cache.has(x)) return cache.get(x);
        const r = fn(x);
        cache.set(x, r);
        return r;
    };
};
