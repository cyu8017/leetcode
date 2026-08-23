// LeetCode 2348 - Number of Zero-Filled Subarrays
// https://leetcode.com/problems/number-of-zero-filled-subarrays/

/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let ans = 0, streak = 0;
    for (const x of nums) {
        if (x === 0) { streak++; ans += streak; }
        else streak = 0;
    }
    return ans;
};
