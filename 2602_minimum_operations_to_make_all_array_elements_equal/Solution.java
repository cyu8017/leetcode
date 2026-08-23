// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

import java.util.Arrays;

class Solution {
    public long[] minOperations(int[] nums, int[] queries) {
        Arrays.sort(nums);
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        long[] ans = new long[queries.length];
        for (int qi = 0; qi < queries.length; ++qi) {
            int q = queries[qi];
            int i = LowerBound(nums, q);
            long left = (long)q * i - pref[i];
            long right = pref[n] - pref[i] - (long)q * (n - i);
            ans[qi] = left + right;
        }
        return ans;
    }

    int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
