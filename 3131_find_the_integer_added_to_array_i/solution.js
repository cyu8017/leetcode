// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var addedInteger = function(nums1, nums2) {
    let min1 = nums1[0], min2 = nums2[0];
    for (const x of nums1) min1 = Math.min(min1, x);
    for (const x of nums2) min2 = Math.min(min2, x);
    return min2 - min1;
};
