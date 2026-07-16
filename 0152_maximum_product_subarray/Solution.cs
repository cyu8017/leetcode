using System;

public class Solution {
    public int MaxProduct(int[] nums) {
        int best = nums[0], max = nums[0], min = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            int value = nums[i], previousMax = max, previousMin = min;
            max = Math.Max(value, Math.Max(previousMax * value, previousMin * value));
            min = Math.Min(value, Math.Min(previousMax * value, previousMin * value));
            best = Math.Max(best, max);
        }
        return best;
    }
}