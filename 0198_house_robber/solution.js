// LeetCode 0198 - House Robber
// https://leetcode.com/problems/house-robber/

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let prev2 = 0;
    let prev1 = 0;
    for (const num of nums) {
        [prev2, prev1] = [prev1, Math.max(prev1, prev2 + num)];
    }
    return prev1;
};