// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

using System;

public class Solution {
    public long MaxStrength(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        if (n == 1) return nums[0];
        long prod = 1;
        bool used = false;
        int i = 0;
        while (i + 1 < n && nums[i] < 0 && nums[i + 1] < 0) {
            prod *= 1L * nums[i] * nums[i + 1];
            used = true;
            i += 2;
        }
        bool negLeft = i < n && nums[i] < 0;
        for (; i < n; i++) {
            if (nums[i] > 0) { prod *= nums[i]; used = true; }
        }
        if (!used) {
            if (negLeft) {
                foreach (int x in nums) if (x == 0) return 0;
                return nums[n - 1];
            }
            return 0;
        }
        return prod;
    }
}
