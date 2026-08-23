// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

var timeLimit = function(fn, t) {
    return async function(...args) {
        return await Promise.race([
            fn(...args),
            new Promise((_, reject) => setTimeout(() => reject("Time Limit Exceeded"), t)),
        ]);
    };
};
