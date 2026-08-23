// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

using System.Collections.Generic;

public class Solution {
    const int MX = 500000;
    static List<int> S;
    static bool inited;

    static void EnsureInit() {
        if (inited) return;
        bool[] isPrime = new bool[MX + 1];
        for (int i = 0; i <= MX; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        var primes = new List<int>();
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) {
                primes.Add(i);
                if (1L * i * i <= MX) {
                    for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
                }
            }
        }
        S = new List<int> { 0 };
        int t = 0;
        foreach (int x in primes) {
            t += x;
            if (t > MX) break;
            if (isPrime[t]) S.Add(t);
        }
        inited = true;
    }

    public int LargestPrime(int n) {
        EnsureInit();
        int lo = 0, hi = S.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (S[mid] <= n) lo = mid + 1;
            else hi = mid;
        }
        return S[lo - 1];
    }
}
