// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1_000_000_007;

    private long modPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    public int maxFrequencyScore(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        long score = 0, best = 0;
        for (int i = 0; i < nums.length; i++) {
            score = add(freq, score, nums[i]);
            if (i >= k) score = remove(freq, score, nums[i - k]);
            if (i >= k - 1 && score > best) best = score;
        }
        return (int) best;
    }

    private long add(Map<Integer, Integer> freq, long score, int x) {
        int c = freq.getOrDefault(x, 0);
        if (c > 0) score = (score - modPow(x, c) + MOD) % MOD;
        freq.put(x, c + 1);
        return (score + modPow(x, c + 1)) % MOD;
    }

    private long remove(Map<Integer, Integer> freq, long score, int x) {
        int c = freq.get(x);
        score = (score - modPow(x, c) + MOD) % MOD;
        if (c == 1) freq.remove(x);
        else {
            freq.put(x, c - 1);
            score = (score + modPow(x, c - 1)) % MOD;
        }
        return score;
    }
}
