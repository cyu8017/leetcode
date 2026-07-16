// LeetCode 0204 - Count Primes\n// https://leetcode.com/problems/\n\nusing System;

public class Solution {
    public int CountPrimes(int n) {
        if (n <= 2) return 0;
        var prime = new bool[n];
        Array.Fill(prime, true);
        for (var p = 2; p * p < n; p++) if (prime[p]) for (var multiple = p * p; multiple < n; multiple += p) prime[multiple] = false;
        var count = 0;
        for (var i = 2; i < n; i++) if (prime[i]) count++;
        return count;
    }
}
