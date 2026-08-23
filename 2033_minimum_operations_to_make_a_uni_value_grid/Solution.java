// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

import java.util.*;

class Solution {
    public int minOperations(int[][] grid, int x) {
        List<Integer> vals = new ArrayList<>();
        int bas = grid[0][0] % x;
        for (int[] row : grid) for (int v : row) {
            if (v % x != bas) return -1;
            vals.add(v);
        }
        Collections.sort(vals);
        int median = vals.get(vals.size() / 2), ans = 0;
        for (int v : vals) ans += Math.abs(v - median) / x;
        return ans;
    }
}
