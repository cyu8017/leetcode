// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

public class Solution {
    public int MinZeroArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        bool Ok(int k) {
            long[] diff = new long[n + 1];
            for (int i = 0; i < k; i++) {
                var q = queries[i];
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
        if (Ok(0)) return 0;
        int lo = 1, hi = queries.Length + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= queries.Length && Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        if (lo > queries.Length) return -1;
        return lo;
    }
}
