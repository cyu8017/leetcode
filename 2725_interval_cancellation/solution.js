// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

var cancellable = function(fn, args, t) {
    fn(...args);
    const id = setInterval(() => fn(...args), t);
    return function() { clearInterval(id); };
};
