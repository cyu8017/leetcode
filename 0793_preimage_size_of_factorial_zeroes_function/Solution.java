// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution {
    public int preimageSizeFZF(int k) {
        return (int) (firstGe(k + 1) - firstGe(k));
    }

    private long zeros(long n) {
        long z = 0;
        while (n > 0) {
            n /= 5;
            z += n;
        }
        return z;
    }

    private long firstGe(long target) {
        long lo = 0, hi = 5L * target + 5;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (zeros(mid) >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
