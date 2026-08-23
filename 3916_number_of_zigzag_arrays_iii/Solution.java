// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    public int zigZagArrays(int n, int l, int r) {
        final long mod = 1000000007;
        int points = n + 1;
        long[] values = new long[points + 1];
        for (int m = 1; m <= points; m++) {
            long[] up = new long[m];
            long[] down = new long[m];
            for (int value = 0; value < m; value++) {
                up[value] = value;
                down[value] = m - 1 - value;
            }
            for (int length = 3; length <= n; length++) {
                long[] nextUp = new long[m];
                long[] nextDown = new long[m];
                long prefix = 0;
                for (int value = 0; value < m; value++) {
                    nextUp[value] = prefix;
                    prefix = (prefix + down[value]) % mod;
                }
                long suffix = 0;
                for (int value = m - 1; value >= 0; value--) {
                    nextDown[value] = suffix;
                    suffix = (suffix + up[value]) % mod;
                }
                up = nextUp;
                down = nextDown;
            }
            for (int value = 0; value < m; value++) {
                values[m] = (values[m] + up[value] + down[value]) % mod;
            }
        }
        long x = (r - l + 1) % mod;
        if (r - l + 1 <= points) return (int) values[r - l + 1];
        long[] prefixA = new long[points + 2];
        long[] suffixA = new long[points + 2];
        prefixA[0] = 1;
        for (int i = 1; i <= points; i++) {
            prefixA[i] = prefixA[i - 1] * ((x - i + mod) % mod) % mod;
        }
        suffixA[points + 1] = 1;
        for (int i = points; i >= 1; i--) {
            suffixA[i] = suffixA[i + 1] * ((x - i + mod) % mod) % mod;
        }
        long[] factorial = new long[points + 1];
        factorial[0] = 1;
        for (int i = 1; i <= points; i++) factorial[i] = factorial[i - 1] * i % mod;
        long answer = 0;
        for (int i = 1; i <= points; i++) {
            long numerator = prefixA[i - 1] * suffixA[i + 1] % mod;
            long denominator = factorial[i - 1] * factorial[points - i] % mod;
            long term = values[i] * numerator % mod * powm(denominator, mod - 2, mod) % mod;
            if ((points - i) % 2 == 1) answer -= term;
            else answer += term;
            answer %= mod;
        }
        if (answer < 0) answer += mod;
        return (int) answer;
    }

    private long powm(long a, long e, long mod) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return res;
    }
}
