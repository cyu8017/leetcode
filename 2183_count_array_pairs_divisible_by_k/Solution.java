// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

import java.util.*;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public long countPairs(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        long ans = 0;
        for (int x : nums) {
            int g1 = gcd(x, k);
            for (Map.Entry<Integer, Integer> kv : freq.entrySet())
                if (1L * g1 * kv.getKey() % k == 0) ans += kv.getValue();
            freq.merge(g1, 1, Integer::sum);
        }
        return ans;
    }
}
