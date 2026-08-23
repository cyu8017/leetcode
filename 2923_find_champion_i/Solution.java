// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

class Solution {
    public int findChampion(int[][] grid) {
        int n = grid.length;
        for (int i = 0; i < n; i++) {
            boolean win = true;
            for (int j = 0; j < n; j++)
                if (i != j && grid[i][j] == 0) {
                    win = false;
                    break;
                }
            if (win) return i;
        }
        return -1;
    }
}
