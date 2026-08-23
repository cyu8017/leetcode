// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int maxNiceDivisors(int primeFactors) {
        if (primeFactors <= 3) {
            return primeFactors;
        }
        if (primeFactors % 3 == 0) {
            return modPow(3, primeFactors / 3);
        }
        if (primeFactors % 3 == 1) {
            return (int) ((long) modPow(3, primeFactors / 3 - 1) * 4 % MOD);
        }
        return (int) ((long) modPow(3, primeFactors / 3) * 2 % MOD);
    }

    private int modPow(int base, int exp) {
        long result = 1;
        long value = base;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * value % MOD;
            }
            value = value * value % MOD;
            exp >>= 1;
        }
        return (int) result;
    }
}
