// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    if (nums.length <= 4) return 0;
    nums.sort((a, b) => a - b);
    let ans = Infinity;
    for (let i = 0; i < 4; i++) {
        ans = Math.min(ans, nums[nums.length - 4 + i] - nums[i]);
    }
    return ans;
};
