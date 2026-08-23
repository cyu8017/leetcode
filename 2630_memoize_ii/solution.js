// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

var memoize = function(fn) {
    const root = new Map();
    const RES = Symbol("res");
    return function(...args) {
        let node = root;
        for (const a of args) {
            if (!node.has(a)) node.set(a, new Map());
            node = node.get(a);
        }
        if (node.has(RES)) return node.get(RES);
        const v = fn(...args);
        node.set(RES, v);
        return v;
    };
};
