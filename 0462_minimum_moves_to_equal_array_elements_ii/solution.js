// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution {
    minMoves2(nums) {
        nums.sort((a, b) => a - b);
        const median = nums[Math.floor(nums.length / 2)];
        return nums.reduce((total, value) => total + Math.abs(value - median), 0);
    }
}

module.exports = { Solution };
