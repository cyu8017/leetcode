// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumStrongPairXor = function(nums) {
    let ans = 0;
    for (let i = 0; i < nums.length; i++)
        for (let j = i; j < nums.length; j++) {
            const x = nums[i], y = nums[j];
            if (Math.abs(x - y) <= Math.min(x, y)) {
                const xorr = x ^ y;
                if (xorr > ans) ans = xorr;
            }
        }
    return ans;
};
