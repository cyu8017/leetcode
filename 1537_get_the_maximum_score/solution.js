// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxSum = function(nums1, nums2) {
    let i = 0, j = 0, first = 0, second = 0;
    while (i < nums1.length || j < nums2.length) {
        if (j === nums2.length || (i < nums1.length && nums1[i] < nums2[j])) {
            first += nums1[i++];
        } else if (i === nums1.length || nums2[j] < nums1[i]) {
            second += nums2[j++];
        } else {
            first = second = Math.max(first, second) + nums1[i];
            i++; j++;
        }
    }
    return Math.max(first, second) % 1000000007;
};
