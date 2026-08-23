// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

public class Solution {
    public int[] FindMissingAndRepeatedValues(int[][] grid) {
        int n = grid.Length;
        int[] freq = new int[n * n + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                freq[grid[i][j]]++;
        int rep = 0, miss = 0;
        for (int i = 1; i <= n * n; i++) {
            if (freq[i] == 2) rep = i;
            if (freq[i] == 0) miss = i;
        }
        return new int[] { rep, miss };
    }
}
