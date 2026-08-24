// LeetCode 2527 - Find Xor-Beauty of Array
// https://leetcode.com/problems/find-xor-beauty-of-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var xorBeauty = function(nums) {
    let ans = 0;
    for (const x of nums) ans ^= x;
    return ans;
};
