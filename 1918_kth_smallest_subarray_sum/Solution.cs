// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

using System;
using System.Linq;

public class Solution {
    public int KthSmallestSubarraySum(int[] nums, int k) {
        int Count(int limit) {
            int total = 0, left = 0, ans = 0;
            for (int right = 0; right < nums.Length; right++) {
                total += nums[right];
                while (total > limit) total -= nums[left++];
                ans += right - left + 1;
            }
            return ans;
        }
        int lo = nums.Min(), hi = nums.Sum();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Count(mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}