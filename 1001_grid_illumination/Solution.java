// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {
        Map<Integer, Integer> rows = new HashMap<>();
        Map<Integer, Integer> cols = new HashMap<>();
        Map<Integer, Integer> diag1 = new HashMap<>();
        Map<Integer, Integer> diag2 = new HashMap<>();
        Set<Long> lit = new HashSet<>();
        for (int[] lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            long key = (((long) r) << 32) | (c & 0xffffffffL);
            if (!lit.add(key)) continue;
            rows.merge(r, 1, Integer::sum);
            cols.merge(c, 1, Integer::sum);
            diag1.merge(r - c, 1, Integer::sum);
            diag2.merge(r + c, 1, Integer::sum);
        }
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int r = queries[qi][0], c = queries[qi][1];
            if (rows.getOrDefault(r, 0) > 0 || cols.getOrDefault(c, 0) > 0
                    || diag1.getOrDefault(r - c, 0) > 0 || diag2.getOrDefault(r + c, 0) > 0) {
                ans[qi] = 1;
            }
            for (int i = r - 1; i <= r + 1; i++) {
                for (int j = c - 1; j <= c + 1; j++) {
                    long key = (((long) i) << 32) | (j & 0xffffffffL);
                    if (lit.remove(key)) {
                        dec(rows, i);
                        dec(cols, j);
                        dec(diag1, i - j);
                        dec(diag2, i + j);
                    }
                }
            }
        }
        return ans;
    }

    private void dec(Map<Integer, Integer> map, int key) {
        int v = map.getOrDefault(key, 0) - 1;
        if (v <= 0) map.remove(key);
        else map.put(key, v);
    }
}
