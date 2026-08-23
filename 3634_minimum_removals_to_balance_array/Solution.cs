// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

using System;

public class Solution {
    public int MinRemoval(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length, cnt = 0;
        for (int i = 0; i < n; i++) {
            int j = n;
            if (1L * nums[i] * k <= nums[n - 1]) {
                long target = 1L * nums[i] * k + 1;
                j = LowerBound(nums, target);
            }
            cnt = Math.Max(cnt, j - i);
        }
        return n - cnt;
    }

    static int LowerBound(int[] a, long target) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
