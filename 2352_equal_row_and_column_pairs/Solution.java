// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String, Integer> freq = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String key = Arrays.toString(grid[i]);
            freq.put(key, freq.getOrDefault(key, 0) + 1);
        }
        int ans = 0;
        int[] col = new int[n];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) col[i] = grid[i][j];
            ans += freq.getOrDefault(Arrays.toString(col), 0);
        }
        return ans;
    }
}
