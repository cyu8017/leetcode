// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

class Solution {
    private static final int M = 50;
    private final long[] cnt = new long[M + 1];
    private final long[] s = new long[M + 1];

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

    private long[] numIdxAndSum(long x) {
        long idx = 0, totalSum = 0;
        while (x > 0) {
            int i = 63 - Long.numberOfLeadingZeros(x);
            idx += cnt[i];
            totalSum += s[i];
            x -= 1L << i;
            totalSum += (x + 1) * i;
            idx += x + 1;
        }
        return new long[]{idx, totalSum};
    }

    private long f(long i) {
        long l = 0, r = 1L << M;
        while (l < r) {
            long mid = (l + r + 1) >> 1;
            long[] p = numIdxAndSum(mid);
            if (p[0] < i) l = mid;
            else r = mid - 1;
        }
        long[] p = numIdxAndSum(l);
        long totalSum = p[1];
        i -= p[0];
        long x = l + 1;
        for (long j = 0; j < i; j++) {
            long y = x & -x;
            totalSum += Long.numberOfTrailingZeros(y);
            x -= y;
        }
        return totalSum;
    }

    private long qpow(long a, long n, long mod) {
        long ans = 1 % mod;
        a %= mod;
        while (n > 0) {
            if ((n & 1) != 0) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ans;
    }

    public int[] findProductsOfElements(long[][] queries) {
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long left = queries[i][0], right = queries[i][1], mod = queries[i][2];
            long power = f(right + 1) - f(left);
            ans[i] = (int) qpow(2, power, mod);
        }
        return ans;
    }
}
