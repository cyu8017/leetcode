// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

using System.Collections.Generic;

public class Solution {
    public bool CanMouseWin(string[] grid, int catJump, int mouseJump) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        int totalOpen = 0;
        int mouse = 0;
        int cat = 0;
        int food = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                char cell = grid[r][c];
                if (cell != '#') totalOpen++;
                if (cell == 'M') mouse = r * cols + c;
                else if (cell == 'C') cat = r * cols + c;
                else if (cell == 'F') food = r * cols + c;
            }
        }
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        int[] ComputeMoves(int pos, int jump) {
            int r = pos / cols;
            int c = pos % cols;
            var outList = new List<int> { pos };
            foreach (int[] dir in dirs) {
                for (int step = 1; step <= jump; step++) {
                    int nr = r + dir[0] * step;
                    int nc = c + dir[1] * step;
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#') break;
                    outList.Add(nr * cols + nc);
                }
            }
            return outList.ToArray();
        }
        int cells = rows * cols;
        var mouseMoves = new int[cells][];
        var catMoves = new int[cells][];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != '#') {
                    int pos = r * cols + c;
                    mouseMoves[pos] = ComputeMoves(pos, mouseJump);
                    catMoves[pos] = ComputeMoves(pos, catJump);
                }
            }
        }
        int maxTurn = 2 * totalOpen;
        var memo = new sbyte[cells * cells * maxTurn];
        bool Win(int m, int c, int turn) {
            if (turn >= maxTurn) return false;
            if (m == food) return true;
            if (c == food || c == m) return false;
            int key = (m * cells + c) * maxTurn + turn;
            if (memo[key] != 0) return memo[key] == 1;
            bool result;
            if (turn % 2 == 0) {
                result = false;
                foreach (int nm in mouseMoves[m]) {
                    if (Win(nm, c, turn + 1)) {
                        result = true;
                        break;
                    }
                }
            } else {
                result = true;
                foreach (int nc in catMoves[c]) {
                    if (!Win(m, nc, turn + 1)) {
                        result = false;
                        break;
                    }
                }
            }
            memo[key] = (sbyte)(result ? 1 : 2);
            return result;
        }
        return Win(mouse, cat, 0);
    }
}
