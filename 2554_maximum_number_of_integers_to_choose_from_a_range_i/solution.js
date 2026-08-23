// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    const ban = new Set(banned);
    let ans = 0, sum = 0;
    for (let i = 1; i <= n; i++) {
        if (ban.has(i)) continue;
        if (sum + i > maxSum) break;
        sum += i;
        ans++;
    }
    return ans;
};
