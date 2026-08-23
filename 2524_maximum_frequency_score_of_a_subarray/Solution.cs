// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;

    long ModPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    public int MaxFrequencyScore(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        long score = 0;

        void Add(int x) {
            int c = freq.GetValueOrDefault(x, 0);
            if (c > 0) score = (score - ModPow(x, c) + MOD) % MOD;
            freq[x] = c + 1;
            score = (score + ModPow(x, c + 1)) % MOD;
        }

        void Remove(int x) {
            int c = freq[x];
            score = (score - ModPow(x, c) + MOD) % MOD;
            if (c == 1) freq.Remove(x);
            else {
                freq[x] = c - 1;
                score = (score + ModPow(x, c - 1)) % MOD;
            }
        }

        long best = 0;
        for (int i = 0; i < nums.Length; i++) {
            Add(nums[i]);
            if (i >= k) Remove(nums[i - k]);
            if (i >= k - 1 && score > best) best = score;
        }
        return (int)best;
    }
}
