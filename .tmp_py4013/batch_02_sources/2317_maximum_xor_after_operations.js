// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumXOR = function(nums) {
    let ans = 0;
    for (const x of nums) ans |= x;
    return ans;
};
