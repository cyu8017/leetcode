// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

export function createCounter(init: any): any {
    let cur = init;
    return {
        increment: function() { return ++cur; },
        decrement: function() { return --cur; },
        reset: function() { cur = init; return cur; },
    };
}
