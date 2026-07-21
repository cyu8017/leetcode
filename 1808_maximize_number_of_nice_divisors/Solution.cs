// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

public class Solution {
    private const int MOD = 1_000_000_007;

    public int MaxNiceDivisors(int primeFactors) {
        if (primeFactors <= 3) return primeFactors;
        if (primeFactors % 3 == 0) return (int)ModPow(3, primeFactors / 3);
        if (primeFactors % 3 == 1) return (int)(ModPow(3, primeFactors / 3 - 1) * 4 % MOD);
        return (int)(ModPow(3, primeFactors / 3) * 2 % MOD);
    }

    private long ModPow(long baseVal, long exp) {
        long result = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) result = result * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return result;
    }
}
