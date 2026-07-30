// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

public class Solution {
    private const int Mod = 1_000_000_007;

    public int NumPrimeArrangements(int n) {
        bool IsPrime(int x) {
            if (x < 2) return false;
            for (int d = 2; d * d <= x; d++) {
                if (x % d == 0) return false;
            }
            return true;
        }

        int primes = 0;
        for (int i = 1; i <= n; i++) {
            if (IsPrime(i)) primes++;
        }
        return (int)(Fact(primes) * Fact(n - primes) % Mod);
    }

    private static long Fact(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) result = result * i % Mod;
        return result;
    }
}
