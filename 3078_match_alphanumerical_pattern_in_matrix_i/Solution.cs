// LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
// https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

public class Solution {
    public int[] FindPattern(int[][] board, string[] pattern) {
        int m = board.Length, n = board[0].Length;
        int r = pattern.Length, c = pattern[0].Length;
        bool Check(int i, int j) {
            int[] d1 = new int[26], d2 = new int[10];
            for (int a = 0; a < r; a++) {
                for (int b = 0; b < c; b++) {
                    int x = i + a, y = j + b;
                    char ch = pattern[a][b];
                    if (ch >= '0' && ch <= '9') {
                        if (ch - '0' != board[x][y]) return false;
                    } else {
                        int v = ch - 'a';
                        if (d1[v] > 0 && d1[v] - 1 != board[x][y]) return false;
                        if (d2[board[x][y]] > 0 && d2[board[x][y]] - 1 != v) return false;
                        d1[v] = board[x][y] + 1;
                        d2[board[x][y]] = v + 1;
                    }
                }
            }
            return true;
        }
        for (int i = 0; i < m - r + 1; i++)
            for (int j = 0; j < n - c + 1; j++)
                if (Check(i, j)) return new[] { i, j };
        return new[] { -1, -1 };
    }
}
