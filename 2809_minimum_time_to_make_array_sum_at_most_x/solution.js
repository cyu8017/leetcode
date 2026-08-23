// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} x
 * @return {number}
 */
var minimumTime = function(nums1, nums2, x) {
    const n = nums1.length;
    const arr = Array.from({length: n}, (_, i) => [nums1[i], nums2[i]]);
    let sum1 = 0, sum2 = 0;
    for (let i = 0; i < n; i++) {
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    arr.sort((a, b) => a[1] - b[1]);
    const dp = Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j >= 1; j--) {
            dp[j] = Math.max(dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1]);
        }
    }
    for (let t = 0; t <= n; t++) {
        if (sum1 + sum2 * t - dp[t] <= x) return t;
    }
    return -1;
};
