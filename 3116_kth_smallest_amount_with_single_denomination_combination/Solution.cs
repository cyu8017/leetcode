// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

public class Solution {
    long Gcdll(long a, long b) {
        while (b != 0) { long t = a % b; a = b; b = t; }
        return a;
    }
    long Lcmll(long a, long b) => a / Gcdll(a, b) * b;

    public long FindKthSmallest(int[] coins, int k) {
        long r = 100000000000L;
        int n = coins.Length;
        bool Check(long mx) {
            long cnt = 0;
            for (int i = 1; i < (1 << n); i++) {
                long v = 1;
                for (int j = 0; j < n; j++) {
                    if (((i >> j) & 1) != 0) {
                        v = Lcmll(v, coins[j]);
                        if (v > mx) break;
                    }
                }
                int m = BitCount(i);
                if (m % 2 == 1) cnt += mx / v;
                else cnt -= mx / v;
            }
            return cnt >= k;
        }
        long lo = 1, hi = r;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (Check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    static int BitCount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }
}
