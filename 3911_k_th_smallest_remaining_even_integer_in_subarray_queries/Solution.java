// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

class Solution {
    public long[] kthSmallestEven(int[] nums, int[][] queries) {
        int n = nums.length;
        var evenPrefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0 ? 1 : 0);
        }
        var ans = new long[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int l = queries[qi][0], r = queries[qi][1];
            long k = queries[qi][2];
            long lo = 1, hi = k + (r - l + 1);
            while (lo < hi) {
                long mid = (lo + hi) / 2;
                int pos = UpperBound(nums, 2 * mid);
                if (pos > r + 1) pos = r + 1;
                int removed = 0;
                if (pos > l) removed = evenPrefix[pos] - evenPrefix[l];
                if (mid - removed >= k) hi = mid;
                else lo = mid + 1;
            }
            ans[qi] = 2 * lo;
        }
        return ans;
    }
    static int UpperBound(int[] a, long x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
