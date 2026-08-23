// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

var createCounter = function(init) {
    let cur = init;
    return {
        increment: function() { return ++cur; },
        decrement: function() { return --cur; },
        reset: function() { cur = init; return cur; },
    };
};
