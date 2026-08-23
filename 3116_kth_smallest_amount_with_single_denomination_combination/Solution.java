// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution {
    private long gcdll(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private long lcmll(long a, long b) {
        return a / gcdll(a, b) * b;
    }

    private int bitCount(int x) {
        int c = 0;
        while (x != 0) {
            c += x & 1;
            x >>= 1;
        }
        return c;
    }

    public long findKthSmallest(int[] coins, int k) {
        long r = 100000000000L;
        int n = coins.length;
        long lo = 1, hi = r;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (check(coins, n, mid, k)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean check(int[] coins, int n, long mx, int k) {
        long cnt = 0;
        for (int i = 1; i < (1 << n); i++) {
            long v = 1;
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) != 0) {
                    v = lcmll(v, coins[j]);
                    if (v > mx) break;
                }
            }
            int m = bitCount(i);
            if (m % 2 == 1) cnt += mx / v;
            else cnt -= mx / v;
        }
        return cnt >= k;
    }
}
