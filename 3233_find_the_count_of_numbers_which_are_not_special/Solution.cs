// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

using System;

public class Solution {
    const int M = 31623;
    static bool[] primes;
    static bool inited;

    static void InitPrimes() {
        if (inited) return;
        primes = new bool[M + 1];
        Array.Fill(primes, true);
        primes[0] = primes[1] = false;
        for (int i = 2; i <= M; i++) {
            if (primes[i]) {
                for (int j = i * 2; j <= M; j += i) primes[j] = false;
            }
        }
        inited = true;
    }

    public int NonSpecialCount(int l, int r) {
        InitPrimes();
        int lo = (int)Math.Ceiling(Math.Sqrt(l));
        int hi = (int)Math.Floor(Math.Sqrt(r));
        int cnt = 0;
        for (int i = lo; i <= hi; i++) {
            if (primes[i]) cnt++;
        }
        return r - l + 1 - cnt;
    }
}
