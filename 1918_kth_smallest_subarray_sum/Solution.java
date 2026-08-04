// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

class Solution {
    public int kthSmallestSubarraySum(int[] nums, int k) {
        int lo = Integer.MAX_VALUE, hi = 0;
        for (int x : nums) {
            lo = Math.min(lo, x);
            hi += x;
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (count(nums, mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int count(int[] nums, int limit) {
        int total = 0, left = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            total += nums[right];
            while (total > limit) total -= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
}
