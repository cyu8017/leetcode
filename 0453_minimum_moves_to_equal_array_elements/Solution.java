// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution {
    public int minMoves(int[] nums) {
        int minimum = nums[0];
        for (int value : nums) {
            minimum = Math.min(minimum, value);
        }
        int moves = 0;
        for (int value : nums) {
            moves += value - minimum;
        }
        return moves;
    }
}
