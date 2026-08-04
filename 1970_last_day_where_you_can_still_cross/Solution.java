// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

import java.util.*;

class Solution {
    public int latestDayToCross(int row, int col, int[][] cells) {
        int lo = 1, hi = cells.length, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can(row, col, cells, mid)) {
                ans = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        return ans;
    }

    private boolean can(int row, int col, int[][] cells, int day) {
        boolean[][] blocked = new boolean[row][col];
        for (int i = 0; i < day; i++) blocked[cells[i][0] - 1][cells[i][1] - 1] = true;
        Deque<int[]> stack = new ArrayDeque<>();
        boolean[][] seen = new boolean[row][col];
        for (int c = 0; c < col; c++) {
            if (!blocked[0][c]) {
                stack.push(new int[]{0, c});
                seen[0][c] = true;
            }
        }
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            if (cur[0] == row - 1) return true;
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                if (nr >= 0 && nc >= 0 && nr < row && nc < col && !blocked[nr][nc] && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}
