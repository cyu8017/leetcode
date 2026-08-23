// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

using System.Collections.Generic;

public class Solution {
    static List<int> primes = new List<int>();
    static void EnsurePrimes() {
        if (primes.Count > 0) return;
        int x = 2;
        while (primes.Count < 1000) {
            bool isPrime = true;
            foreach (int p in primes) {
                if (p * p > x) break;
                if (x % p == 0) { isPrime = false; break; }
            }
            if (isPrime) primes.Add(x);
            x++;
        }
    }
    public int MinNumberOfPrimes(int n, int m) {
        EnsurePrimes();
        const int Inf = int.MaxValue / 2;
        int[] f = new int[n + 1];
        for (int i = 0; i <= n; i++) f[i] = Inf;
        f[0] = 0;
        for (int pi = 0; pi < m; pi++) {
            int x = primes[pi];
            for (int i = x; i <= n; i++)
                if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1;
        }
        return f[n] < Inf ? f[n] : -1;
    }
}
