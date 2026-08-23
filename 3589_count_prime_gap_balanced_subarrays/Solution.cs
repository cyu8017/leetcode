// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

using System;
using System.Collections.Generic;

public class Solution {
    public int PrimeSubarray(int[] nums, int k) {
        int mx = 0;
        foreach (int v in nums) mx = Math.Max(mx, v);
        bool[] isPrime = new bool[mx + 1];
        for (int i = 2; i <= mx; i++) isPrime[i] = true;
        for (int i = 2; i * i <= mx; i++)
            if (isPrime[i])
                for (int j = i * i; j <= mx; j += i) isPrime[j] = false;
        int n = nums.Length, ans = 0;
        for (int l = 0; l < n; l++) {
            var primes = new List<int>();
            for (int r = l; r < n; r++) {
                if (isPrime[nums[r]]) primes.Add(nums[r]);
                if (primes.Count >= 2) {
                    int mn = primes[0], mxp = primes[0];
                    foreach (int p in primes) {
                        mn = Math.Min(mn, p);
                        mxp = Math.Max(mxp, p);
                    }
                    if (mxp - mn <= k) ans++;
                }
            }
        }
        return ans;
    }
}
