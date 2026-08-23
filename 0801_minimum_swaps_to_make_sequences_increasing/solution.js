// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSwap = function(nums1, nums2) {
    const n = nums1.length;
    const swap = new Array(n).fill(n);
    const keep = new Array(n).fill(n);
    swap[0] = 1;
    keep[0] = 0;
    for (let i = 1; i < n; i++) {
        if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
            keep[i] = keep[i - 1];
            swap[i] = swap[i - 1] + 1;
        }
        if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
            keep[i] = Math.min(keep[i], swap[i - 1]);
            swap[i] = Math.min(swap[i], keep[i - 1] + 1);
        }
    }
    return Math.min(swap[n - 1], keep[n - 1]);
};
