// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let adds = 0, maxBits = 0;
    for (const x of nums) {
        let v = x, bits = 0, ones = 0;
        while (v > 0) {
            ones += v & 1;
            v >>= 1;
            bits++;
        }
        adds += ones;
        if (bits > 0) maxBits = Math.max(maxBits, bits - 1);
    }
    return adds + maxBits;
};
