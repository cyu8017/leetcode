// LeetCode 2778 - Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (n % (i + 1) === 0) ans += nums[i] * nums[i];
    }
    return ans;
};
