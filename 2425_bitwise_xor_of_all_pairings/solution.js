// LeetCode 2425 - Bitwise XOR of All Pairings
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function(nums1, nums2) {
    let ans = 0;
    if (nums2.length % 2 === 1) for (const x of nums1) ans ^= x;
    if (nums1.length % 2 === 1) for (const x of nums2) ans ^= x;
    return ans;
};
