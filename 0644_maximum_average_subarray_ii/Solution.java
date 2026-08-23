// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double left = nums[0];
        double right = nums[0];
        for (int num : nums) {
            left = Math.min(left, num);
            right = Math.max(right, num);
        }
        for (int i = 0; i < 80; ++i) {
            double mid = (left + right) / 2.0;
            if (canReach(nums, k, mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private boolean canReach(int[] nums, int k, double mid) {
        double prefix = 0.0;
        for (int i = 0; i < k; ++i) {
            prefix += nums[i] - mid;
        }
        if (prefix >= 0) {
            return true;
        }
        double prev = 0.0;
        double minPrev = 0.0;
        for (int i = k; i < nums.length; ++i) {
            prefix += nums[i] - mid;
            prev += nums[i - k] - mid;
            minPrev = Math.min(minPrev, prev);
            if (prefix - minPrev >= 0) {
                return true;
            }
        }
        return false;
    }
}
