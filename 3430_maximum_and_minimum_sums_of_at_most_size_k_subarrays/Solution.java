// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution {
    public long minMaxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int mn = nums[i], mx = nums[i];
            for (int j = i; j < n && j - i + 1 <= k; j++) {
                if (nums[j] < mn) mn = nums[j];
                if (nums[j] > mx) mx = nums[j];
                ans += mn + mx;
            }
        }
        return ans;
    }
}
