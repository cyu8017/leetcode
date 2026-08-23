// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

import java.util.List;

class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();
        for (int i = 0; i + 2 * k <= n; i++) {
            if (inc(nums, i, k) && inc(nums, i + k, k)) return true;
        }
        return false;
    }

    private boolean inc(List<Integer> nums, int start, int k) {
        for (int i = start; i + 1 < start + k; i++) {
            if (nums.get(i) >= nums.get(i + 1)) return false;
        }
        return true;
    }
}
