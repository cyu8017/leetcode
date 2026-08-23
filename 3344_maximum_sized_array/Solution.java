// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

class Solution {
    private boolean ok(long n, long s) {
        long sum = 0;
        for (long i = 0; i < n; i++) {
            for (long j = 0; j < n; j++) {
                long ij = i | j;
                sum += ij * (n - 1) * n / 2;
                if (sum > s) return false;
            }
        }
        return sum <= s;
    }

    public int maxSizedArray(long s) {
        long lo = 1, hi = 2000;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (ok(mid, s)) lo = mid;
            else hi = mid - 1;
        }
        return (int) lo;
    }
}
