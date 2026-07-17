// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution {
    public int waysToSplit(int[] nums) {
        final int mod = 1_000_000_007;
        int n = nums.length;
        long[] prefix = new long[n];
        long total = 0;
        for (int i = 0; i < n; i++) {
            total += nums[i];
            prefix[i] = total;
        }
        long ans = 0;
        for (int i = 0; i < n - 2; i++) {
            long left = prefix[i];
            int lo = lowerBound(prefix, 2 * left, i + 1, n - 1);
            int hi = upperBound(prefix, (total + left) / 2, lo, n - 1);
            ans = (ans + hi - lo) % mod;
        }
        return (int) ans;
    }

    private int lowerBound(long[] prefix, long target, int lo, int hi) {
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (prefix[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    private int upperBound(long[] prefix, long target, int lo, int hi) {
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (prefix[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
