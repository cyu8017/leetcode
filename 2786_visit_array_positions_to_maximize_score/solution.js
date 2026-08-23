// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var maxScore = function(nums, x) {
    const NEG = -1e18;
    let even = nums[0], odd = nums[0];
    if (nums[0] % 2 === 0) odd = NEG;
    else even = NEG;
    for (let i = 1; i < nums.length; i++) {
        const v = nums[i];
        if (nums[i] % 2 === 0) even = Math.max(even + v, odd + v - x);
        else odd = Math.max(odd + v, even + v - x);
    }
    return Math.max(even, odd);
};
