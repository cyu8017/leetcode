// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

var cancellable = function(fn, args, t) {
    const timer = setTimeout(() => fn(...args), t);
    return function() { clearTimeout(timer); };
};
