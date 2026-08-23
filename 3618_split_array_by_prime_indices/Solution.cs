// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

using System;

public class Solution {
    const int M = 100010;
    static bool[] primesCache;

    static bool[] Primes() {
        if (primesCache == null) {
            primesCache = new bool[M];
            Array.Fill(primesCache, true);
            primesCache[0] = primesCache[1] = false;
            for (int i = 2; i < M; i++)
                if (primesCache[i])
                    for (int j = i + i; j < M; j += i) primesCache[j] = false;
        }
        return primesCache;
    }

    public long SplitArray(int[] nums) {
        var pr = Primes();
        long ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (pr[i]) ans += nums[i];
            else ans -= nums[i];
        }
        return Math.Abs(ans);
    }
}
