// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countTrapezoids(int[][] points) {
        final int MOD = 1_000_000_007;
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int[] p : points) cnt.merge(p[1], 1, Integer::sum);
        long ans = 0, pre = 0;
        for (int c : cnt.values()) {
            long lines = (long) c * (c - 1) / 2;
            ans = (ans + pre * lines) % MOD;
            pre = (pre + lines) % MOD;
        }
        return (int) ans;
    }
}
