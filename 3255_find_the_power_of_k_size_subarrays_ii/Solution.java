// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        if (k == 1) return nums;
        int streak = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1] + 1) streak++;
            else streak = 1;
            if (i >= k - 1) ans[i - k + 1] = streak >= k ? nums[i] : -1;
        }
        return ans;
    }
}
