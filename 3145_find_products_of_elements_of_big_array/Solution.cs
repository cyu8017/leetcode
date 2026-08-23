// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

public class Solution {
    const int M = 50;
    long[] cnt = new long[M + 1];
    long[] s = new long[M + 1];

    public Solution() {
        long p = 1;
        cnt[0] = 0;
        s[0] = 0;
        for (int i = 1; i <= M; i++) {
            cnt[i] = cnt[i - 1] * 2 + p;
            s[i] = s[i - 1] * 2 + p * (i - 1);
            p *= 2;
        }
    }

    (long, long) NumIdxAndSum(long x) {
        long idx = 0, totalSum = 0;
        while (x > 0) {
            int i = 63 - LeadingZeroCount((ulong)x);
            idx += cnt[i];
            totalSum += s[i];
            x -= 1L << i;
            totalSum += (x + 1) * i;
            idx += x + 1;
        }
        return (idx, totalSum);
    }

    long F(long i) {
        long l = 0, r = 1L << M;
        while (l < r) {
            long mid = (l + r + 1) >> 1;
            var (idx, _) = NumIdxAndSum(mid);
            if (idx < i) l = mid;
            else r = mid - 1;
        }
        var (_, totalSum) = NumIdxAndSum(l);
        var (idx2, __) = NumIdxAndSum(l);
        i -= idx2;
        long x = l + 1;
        for (long j = 0; j < i; j++) {
            long y = x & -x;
            totalSum += TrailingZeroCount((ulong)y);
            x -= y;
        }
        return totalSum;
    }

    long Qpow(long a, long n, long mod) {
        long ans = 1 % mod;
        a %= mod;
        while (n > 0) {
            if ((n & 1) != 0) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }

    public int[] FindProductsOfElements(long[][] queries) {
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            long left = queries[i][0], right = queries[i][1], mod = queries[i][2];
            long power = F(right + 1) - F(left);
            ans[i] = (int)Qpow(2, power, mod);
        }
        return ans;
    }

    static int LeadingZeroCount(ulong x) {
        if (x == 0) return 64;
        int c = 0;
        if ((x >> 32) == 0) { c += 32; x <<= 32; }
        if ((x >> 48) == 0) { c += 16; x <<= 16; }
        if ((x >> 56) == 0) { c += 8; x <<= 8; }
        if ((x >> 60) == 0) { c += 4; x <<= 4; }
        if ((x >> 62) == 0) { c += 2; x <<= 2; }
        if ((x >> 63) == 0) c += 1;
        return c;
    }

    static int TrailingZeroCount(ulong x) {
        if (x == 0) return 64;
        int c = 0;
        while ((x & 1) == 0) { c++; x >>= 1; }
        return c;
    }
}
