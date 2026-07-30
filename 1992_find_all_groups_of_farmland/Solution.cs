// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

using System.Collections.Generic;

public class Solution {
    public int[][] FindFarmland(int[][] land) {
        int m = land.Length, n = land[0].Length;
        var ans = new List<int[]>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1 && (i == 0 || land[i - 1][j] == 0) && (j == 0 || land[i][j - 1] == 0)) {
                    int r = i, c = j;
                    while (r + 1 < m && land[r + 1][j] == 1) r++;
                    while (c + 1 < n && land[i][c + 1] == 1) c++;
                    ans.Add(new[] { i, j, r, c });
                }
            }
        }
        return ans.ToArray();
    }
}