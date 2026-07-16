// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

public class Solution {
    public int MinMoves2(int[] nums) {
        Array.Sort(nums);
        int median = nums[nums.Length / 2];
        int moves = 0;
        foreach (int value in nums) {
            moves += Math.Abs(value - median);
        }
        return moves;
    }
}
