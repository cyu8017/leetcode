// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

public class Solution {
    public int MaxValueAfterReverse(int[] nums) {
        int baseSum = 0;
        for (int i = 0; i < nums.Length - 1; i++)
            baseSum += System.Math.Abs(nums[i] - nums[i + 1]);
        int gain = 0, low = int.MaxValue, high = int.MinValue;
        for (int i = 0; i < nums.Length - 1; i++) {
            int a = nums[i], b = nums[i + 1];
            gain = System.Math.Max(gain, System.Math.Abs(nums[0] - b) - System.Math.Abs(a - b));
            gain = System.Math.Max(gain, System.Math.Abs(nums[nums.Length - 1] - a) - System.Math.Abs(a - b));
            low = System.Math.Min(low, System.Math.Max(a, b));
            high = System.Math.Max(high, System.Math.Min(a, b));
        }
        return baseSum + System.Math.Max(gain, 2 * (high - low));
    }
}
