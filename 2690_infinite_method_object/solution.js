// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

var createInfiniteObject = function() {
    return new Proxy({}, {
        get: () => () => "Hello World",
    });
};
