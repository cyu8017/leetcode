// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] minAbsDiff(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][] ans = new int[m - k + 1][];
        for (int i = 0; i <= m - k; i++) ans[i] = new int[n - k + 1];
        for (int i = 0; i <= m - k; i++) {
            for (int j = 0; j <= n - k; j++) {
                var nums = new ArrayList<Integer>();
                for (int x = i; x < i + k; x++)
                    for (int y = j; y < j + k; y++) nums.add(grid[x][y]);
                nums.sort(null);
                int d = Integer.MAX_VALUE;
                for (int t = 1; t < nums.size(); t++) {
                    if (nums.get(t) != nums.get(t - 1)) d = Math.min(d, Math.abs(nums.get(t) - nums.get(t - 1)));
                }
                if (d != Integer.MAX_VALUE) ans[i][j] = d;
            }
        }
        return ans;
    }
}
