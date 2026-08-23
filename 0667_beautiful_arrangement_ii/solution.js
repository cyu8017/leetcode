// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/

/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var constructArray = function(n, k) {
    const res = Array(n).fill(0);
    let idx = 0;
    for (let i = 1; i <= n - k; ++i) res[idx++] = i;
    let left = n - k + 1, right = n;
    let takeHigh = true;
    while (left <= right) {
        if (takeHigh) res[idx++] = right--;
        else res[idx++] = left++;
        takeHigh = !takeHigh;
    }
    return res;
};
