// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    public int numPrimeArrangements(int n) {
        final int MOD = 1_000_000_007;
        int primes = 0;
        for (int i = 1; i <= n; i++) if (isPrime(i)) primes++;
        return (int) (fact(primes, MOD) * fact(n - primes, MOD) % MOD);
    }
    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int d = 2; d * d <= x; d++) if (x % d == 0) return false;
        return true;
    }
    private long fact(int n, int MOD) {
        long ans = 1;
        for (int i = 2; i <= n; i++) ans = ans * i % MOD;
        return ans;
    }
}
