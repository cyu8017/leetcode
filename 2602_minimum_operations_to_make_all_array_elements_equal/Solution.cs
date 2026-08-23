// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

using System;

public class Solution {
    public long[] MinOperations(int[] nums, int[] queries) {
        Array.Sort(nums);
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        long[] ans = new long[queries.Length];
        for (int qi = 0; qi < queries.Length; ++qi) {
            int q = queries[qi];
            int i = LowerBound(nums, q);
            long left = (long)q * i - pref[i];
            long right = pref[n] - pref[i] - (long)q * (n - i);
            ans[qi] = left + right;
        }
        return ans;
    }

    int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
