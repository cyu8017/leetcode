// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

using System.Collections.Generic;

public class Solution {
    public int[] ClosestPrimes(int left, int right) {
        bool[] isPrime = new bool[right + 1];
        for (int i = 0; i <= right; i++) isPrime[i] = true;
        if (right >= 0) isPrime[0] = false;
        if (right >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= right; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= right; j += i) isPrime[j] = false;
            }
        }
        var primes = new List<int>();
        for (int i = left; i <= right; i++) if (isPrime[i]) primes.Add(i);
        if (primes.Count < 2) return new[] { -1, -1 };
        int[] best = { primes[0], primes[1] };
        int diff = primes[1] - primes[0];
        for (int i = 1; i + 1 < primes.Count; i++) {
            int d = primes[i + 1] - primes[i];
            if (d < diff) {
                diff = d;
                best = new[] { primes[i], primes[i + 1] };
            }
        }
        return best;
    }
}
