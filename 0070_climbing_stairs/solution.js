// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n <= 2) {
        return n;
    }

    let prev = 1;
    let curr = 2;

    for (let i = 3; i <= n; i++) {
        const next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
};
