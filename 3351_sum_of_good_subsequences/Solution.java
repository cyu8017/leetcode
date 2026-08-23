// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int sumOfGoodSubsequences(int[] nums) {
        final int mod = 1_000_000_007;
        Map<Integer, Integer> cnt = new HashMap<>();
        Map<Integer, Integer> sum = new HashMap<>();
        int ans = 0;
        for (int x : nums) {
            int c = 1;
            int s = x;
            if (cnt.getOrDefault(x - 1, 0) > 0) {
                c = (c + cnt.get(x - 1)) % mod;
                s = (int) (((long) s + sum.get(x - 1) + (long) cnt.get(x - 1) * x % mod) % mod);
            }
            if (cnt.getOrDefault(x + 1, 0) > 0) {
                c = (c + cnt.get(x + 1)) % mod;
                s = (int) (((long) s + sum.get(x + 1) + (long) cnt.get(x + 1) * x % mod) % mod);
            }
            cnt.put(x, (cnt.getOrDefault(x, 0) + c) % mod);
            sum.put(x, (sum.getOrDefault(x, 0) + s) % mod);
            ans = (ans + s) % mod;
        }
        return ans;
    }
}
