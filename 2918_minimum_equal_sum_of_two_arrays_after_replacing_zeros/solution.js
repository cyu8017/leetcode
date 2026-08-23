// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minSum = function(nums1, nums2) {
    let s1 = 0, s2 = 0, z1 = 0, z2 = 0;
    for (const v of nums1) {
        if (v === 0) { z1++; s1++; }
        else s1 += v;
    }
    for (const v of nums2) {
        if (v === 0) { z2++; s2++; }
        else s2 += v;
    }
    if (z1 === 0 && s1 < s2) return -1;
    if (z2 === 0 && s2 < s1) return -1;
    return s1 > s2 ? s1 : s2;
};
