// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findLength = function(nums1, nums2) {
    const m = nums1.length, n = nums2.length;
    let best = 0;
    let dp = new Array(n + 1).fill(0);
    for (let i = 1; i <= m; i++) {
        const next = new Array(n + 1).fill(0);
        for (let j = 1; j <= n; j++) {
            if (nums1[i - 1] === nums2[j - 1]) {
                next[j] = dp[j - 1] + 1;
                best = Math.max(best, next[j]);
            }
        }
        dp = next;
    }
    return best;
};
