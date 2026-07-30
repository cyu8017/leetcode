// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

using System.Collections.Generic;

public class Solution {
    public int LatestDayToCross(int row, int col, int[][] cells) {
        bool Can(int day) {
            var blocked = new HashSet<(int, int)>();
            for (int i = 0; i < day; i++) blocked.Add((cells[i][0] - 1, cells[i][1] - 1));
            var stack = new Stack<(int, int)>();
            var seen = new HashSet<(int, int)>();
            for (int c = 0; c < col; c++) {
                if (!blocked.Contains((0, c))) {
                    stack.Push((0, c));
                    seen.Add((0, c));
                }
            }
            int[] dr = { -1, 1, 0, 0 }, dc = { 0, 0, -1, 1 };
            while (stack.Count > 0) {
                var (r, c) = stack.Pop();
                if (r == row - 1) return true;
                for (int i = 0; i < 4; i++) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && !blocked.Contains((nr, nc)) && seen.Add((nr, nc)))
                        stack.Push((nr, nc));
                }
            }
            return false;
        }
        int lo = 1, hi = cells.Length, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (Can(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
}