// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public int maxScore(int[][] grid) {
        int m = grid.length;
        Map<Integer, List<Integer>> vals = new HashMap<>();
        for (int i = 0; i < m; i++) {
            Set<Integer> seen = new HashSet<>();
            for (int v : grid[i]) {
                if (seen.add(v)) {
                    vals.computeIfAbsent(v, z -> new ArrayList<>()).add(i);
                }
            }
        }
        List<Integer> arr = new ArrayList<>(vals.keySet());
        arr.sort(Collections.reverseOrder());
        int N = 1 << m;
        int[] dp = new int[N];
        for (int v : arr) {
            int[] ndp = dp.clone();
            for (int r : vals.get(v)) {
                int bit = 1 << r;
                for (int mask = 0; mask < N; mask++) {
                    if ((mask & bit) != 0) continue;
                    int cand = dp[mask] + v;
                    int nmask = mask | bit;
                    if (cand > ndp[nmask]) ndp[nmask] = cand;
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int x : dp) ans = Math.max(ans, x);
        return ans;
    }
}
