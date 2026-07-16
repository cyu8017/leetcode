// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution {
    minMoves(nums) {
        const minimum = Math.min(...nums);
        return nums.reduce((total, value) => total + value - minimum, 0);
    }
}

module.exports = { Solution };
