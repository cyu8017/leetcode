// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        double left = nums[0], right = nums[0];
        foreach (int num in nums) {
            if (num < left) left = num;
            if (num > right) right = num;
        }
        for (int i = 0; i < 80; ++i) {
            double mid = (left + right) / 2.0;
            if (CanReach(nums, k, mid)) left = mid;
            else right = mid;
        }
        return left;
    }

    private bool CanReach(int[] nums, int k, double mid) {
        double prefix = 0.0;
        for (int i = 0; i < k; ++i) prefix += nums[i] - mid;
        if (prefix >= 0) return true;
        double prev = 0.0, minPrev = 0.0;
        for (int i = k; i < nums.Length; ++i) {
            prefix += nums[i] - mid;
            prev += nums[i - k] - mid;
            if (prev < minPrev) minPrev = prev;
            if (prefix - minPrev >= 0) return true;
        }
        return false;
    }
}
