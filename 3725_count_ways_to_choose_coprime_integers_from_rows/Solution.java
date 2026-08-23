// LeetCode 3725 - Count Ways To Choose Coprime Integers From Rows
// https://leetcode.com/problems/count_ways_to_choose_coprime_integers_from_rows/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countCoprime(int[][] mat) {
        final int MOD = 1_000_000_007;
        int m = mat.length;
        Map<Integer, Integer> dp = new HashMap<>();
        for (int v : mat[0]) dp.merge(v, 1, Integer::sum);
        for (int i = 1; i < m; i++) {
            Map<Integer, Integer> ndp = new HashMap<>();
            for (int v : mat[i]) {
                for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                    int ng = gcd(e.getKey(), v);
                    ndp.merge(ng, e.getValue(), (a, b) -> (a + b) % MOD);
                }
            }
            dp = ndp;
        }
        return dp.getOrDefault(1, 0);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
