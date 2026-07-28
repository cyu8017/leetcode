// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

using System;

public class Solution {
    public int LargestSumAfterKNegations(int[] nums, int k) {
        Array.Sort(nums);
        for (int i = 0; i < nums.Length && k > 0; i++) {
            if (nums[i] < 0) {
                nums[i] = -nums[i];
                k--;
            }
        }
        if (k % 2 == 1) {
            Array.Sort(nums);
            nums[0] = -nums[0];
        }
        int sum = 0;
        foreach (int x in nums) sum += x;
        return sum;
    }
}
