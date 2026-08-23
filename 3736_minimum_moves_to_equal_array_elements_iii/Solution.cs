// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

using System;

public class Solution {
    public int MinMoves(int[] nums) {
        int mx = 0, s = 0;
        foreach (int x in nums) {
            mx = Math.Max(mx, x);
            s += x;
        }
        return mx * nums.Length - s;
    }
}
