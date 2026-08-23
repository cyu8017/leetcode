// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int rangeSum(int[] nums) {
        final int mod = 1_000_000_007;
        Map<Integer, Integer> cnt = new HashMap<>();
        Map<Integer, Integer> sum = new HashMap<>();
        int ans = 0;
        for (int x : nums) {
            int cL = cnt.getOrDefault(x - 1, 0), sL = sum.getOrDefault(x - 1, 0);
            int cR = cnt.getOrDefault(x + 1, 0), sR = sum.getOrDefault(x + 1, 0);
            int c = (1 + cL + cR) % mod;
            int s = (int) (((long) x + sL + (long) cL * x % mod + sR + (long) cR * x % mod) % mod);
            if (cL > 0 && cR > 0) {
                c = (c + (int) ((long) cL * cR % mod)) % mod;
                s = (int) ((s + (long) sL * cR % mod + (long) sR * cL % mod + (long) cL * cR % mod * x % mod) % mod);
            }
            cnt.put(x, (cnt.getOrDefault(x, 0) + c) % mod);
            sum.put(x, (sum.getOrDefault(x, 0) + s) % mod);
            ans = (ans + s) % mod;
        }
        return ans;
    }
}
