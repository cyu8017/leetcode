// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        if (ok(0, nums, queries, n)) return 0;
        int lo = 1, hi = queries.length + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= queries.length && ok(mid, nums, queries, n)) hi = mid;
            else lo = mid + 1;
        }
        if (lo > queries.length) return -1;
        return lo;
    }

    private boolean ok(int k, int[] nums, int[][] queries, int n) {
        long[] diff = new long[n + 1];
        for (int i = 0; i < k; i++) {
            int[] q = queries[i];
            diff[q[0]] += q[2];
            diff[q[1] + 1] -= q[2];
        }
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    }
}
