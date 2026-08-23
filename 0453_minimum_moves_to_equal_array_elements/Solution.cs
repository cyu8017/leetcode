// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

using System.Linq;

public class Solution {
    public int MinMoves(int[] nums) {
        int minimum = nums.Min();
        int moves = 0;
        foreach (int value in nums) {
            moves += value - minimum;
        }
        return moves;
    }
}
