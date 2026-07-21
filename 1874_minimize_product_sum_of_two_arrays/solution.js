// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minProductSum = function(nums1, nums2) {
    nums1 = nums1.slice().sort((a, b) => a - b);
    nums2 = nums2.slice().sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < nums1.length; i++) sum += nums1[i] * nums2[i];
    return sum;
};
