// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minNumber = function(nums1, nums2) {
    const s1 = new Set(nums1), s2 = new Set(nums2);
    let common = 10;
    for (const x of s1) if (s2.has(x) && x < common) common = x;
    if (common < 10) return common;
    let a = 10, b = 10;
    for (const x of nums1) if (x < a) a = x;
    for (const x of nums2) if (x < b) b = x;
    return Math.min(a * 10 + b, b * 10 + a);
};
