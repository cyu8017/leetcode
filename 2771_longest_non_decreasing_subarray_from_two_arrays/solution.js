// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxNonDecreasingLength = function(nums1, nums2) {
    const n = nums1.length;
    let dp1 = 1, dp2 = 1, ans = 1;
    for (let i = 1; i < n; i++) {
        let nd1 = 1, nd2 = 1;
        if (nums1[i] >= nums1[i - 1]) nd1 = Math.max(nd1, dp1 + 1);
        if (nums1[i] >= nums2[i - 1]) nd1 = Math.max(nd1, dp2 + 1);
        if (nums2[i] >= nums1[i - 1]) nd2 = Math.max(nd2, dp1 + 1);
        if (nums2[i] >= nums2[i - 1]) nd2 = Math.max(nd2, dp2 + 1);
        dp1 = nd1;
        dp2 = nd2;
        ans = Math.max(ans, dp1, dp2);
    }
    return ans;
};
