// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    public int minOperations(int[] nums, int x, int y) {
        int lo = 0, hi = 0;
        for (int v : nums) {
            hi = Math.max(hi, (v + y - 1) / y);
            hi = Math.max(hi, (v + x - 1) / x);
        }
        hi += nums.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(nums, x, y, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(int[] nums, int x, int y, int ops) {
        long extra = 0;
        for (int v : nums) {
            long remain = v - 1L * ops * y;
            if (remain > 0) extra += (remain + (x - y) - 1) / (x - y);
        }
        return extra <= ops;
    }
}
