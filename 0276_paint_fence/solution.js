// LeetCode 0276 - Paint Fence
// https://leetcode.com/problems/paint-fence/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numWays = function(n, k) {
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return k;
    }
    if (n === 2) {
        return k * k;
    }
    let prev2 = k;
    let prev1 = k * k;
    for (let i = 3; i <= n; i++) {
        const next = (prev1 + prev2) * (k - 1);
        prev2 = prev1;
        prev1 = next;
    }
    return prev1;
};
