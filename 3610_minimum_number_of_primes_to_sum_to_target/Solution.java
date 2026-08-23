// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static List<Integer> primes = new ArrayList<Integer>();
    static void ensurePrimes() {
        if (primes.size() > 0) return;
        int x = 2;
        while (primes.size() < 1000) {
            boolean isPrime = true;
            for (int p : primes) {
                if (p * p > x) break;
                if (x % p == 0) { isPrime = false; break; }
            }
            if (isPrime) primes.add(x);
            x++;
        }
    }
    public int minNumberOfPrimes(int n, int m) {
        ensurePrimes();
        final int Inf = Integer.MAX_VALUE / 2;
        int[] f = new int[n + 1];
        for (int i = 0; i <= n; i++) f[i] = Inf;
        f[0] = 0;
        for (int pi = 0; pi < m; pi++) {
            int x = primes.get(pi);
            for (int i = x; i <= n; i++)
                if (f[i - x] + 1 < f[i]) f[i] = f[i - x] + 1;
        }
        return f[n] < Inf ? f[n] : -1;
    }
}
