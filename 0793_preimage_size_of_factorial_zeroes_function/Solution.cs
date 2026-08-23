// LeetCode 0793 - Preimage Size of Factorial Zeroes Function
// https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

public class Solution {
    public int PreimageSizeFZF(int k) {
        return Zeros(FirstGe(k)) == k ? 5 : 0;
    }

    private long Zeros(long x) {
        long count = 0;
        while (x > 0) { x /= 5; count += x; }
        return count;
    }

    private long FirstGe(long target) {
        long lo = 0, hi = 5L * (target + 1);
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (Zeros(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
