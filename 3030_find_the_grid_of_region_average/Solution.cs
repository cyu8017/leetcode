// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

using System;

public class Solution {
    public int[][] ResultGrid(int[][] image, int threshold) {
        int n = image.Length, m = image[0].Length;
        int[][] ans = new int[n][];
        int[][] ct = new int[n][];
        for (int i = 0; i < n; i++) {
            ans[i] = new int[m];
            ct[i] = new int[m];
        }
        for (int i = 0; i + 2 < n; i++) {
            for (int j = 0; j + 2 < m; j++) {
                bool region = true;
                for (int k = 0; k < 3; k++)
                    for (int l = 0; l < 2; l++)
                        region = region && Math.Abs(image[i + k][j + l] - image[i + k][j + l + 1]) <= threshold;
                for (int k = 0; k < 2; k++)
                    for (int l = 0; l < 3; l++)
                        region = region && Math.Abs(image[i + k][j + l] - image[i + k + 1][j + l]) <= threshold;
                if (region) {
                    int tot = 0;
                    for (int k = 0; k < 3; k++)
                        for (int l = 0; l < 3; l++)
                            tot += image[i + k][j + l];
                    for (int k = 0; k < 3; k++)
                        for (int l = 0; l < 3; l++) {
                            ct[i + k][j + l]++;
                            ans[i + k][j + l] += tot / 9;
                        }
                }
            }
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (ct[i][j] == 0) ans[i][j] = image[i][j];
                else ans[i][j] /= ct[i][j];
            }
        return ans;
    }
}
