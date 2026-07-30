// LeetCode 1413 - Minimum Value To Get Positive Step By Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

public class Solution {
    public int MinStartValue(int[] nums) {
        int prefix = 0, lowest = 0;
        foreach (int value in nums) { prefix += value; lowest = System.Math.Min(lowest, prefix); }
        return 1 - lowest;
    }
}
