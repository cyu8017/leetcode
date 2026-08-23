// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

var climbStairs = function(n, costs) {
    const inf = 1e9;
    const f = new Array(n + 1).fill(inf);
    f[0] = 0;
    for (let i = 1; i <= n; i++) {
        const x = costs[i - 1];
        for (let j = Math.max(0, i - 3); j < i; j++) {
            f[i] = Math.min(f[i], f[j] + x + (i - j) * (i - j));
        }
    }
    return f[n];
};
