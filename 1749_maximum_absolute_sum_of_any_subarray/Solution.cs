// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

public class Solution {
    public int MaxAbsoluteSum(int[] nums) {
        int prefix = 0;
        int low = 0;
        int high = 0;
        foreach (int value in nums) {
            prefix += value;
            low = Math.Min(low, prefix);
            high = Math.Max(high, prefix);
        }
        return high - low;
    }
}
