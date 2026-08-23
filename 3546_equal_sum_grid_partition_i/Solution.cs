// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

public class Solution {
    public bool CanPartitionGrid(int[][] grid) {
        long s = 0;
        foreach (var row in grid) foreach (int x in row) s += x;
        if (s % 2 != 0) return false;
        int m = grid.Length, n = grid[0].Length;
        long pre = 0;
        for (int i = 0; i < m; i++) {
            foreach (int x in grid[i]) pre += x;
            if (pre * 2 == s && i + 1 < m) return true;
        }
        pre = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) pre += grid[i][j];
            if (pre * 2 == s && j + 1 < n) return true;
        }
        return false;
    }
}
