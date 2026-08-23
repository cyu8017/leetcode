// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

using System.Text;

public class Solution {
    public bool PlaceWordInCrossword(char[][] board, string word) {
        int m = board.Length, n = board[0].Length, L = word.Length;
        bool Match(string cells) {
            if (cells.Length != L) return false;
            bool ok1 = true, ok2 = true;
            for (int i = 0; i < L; i++) {
                if (cells[i] != ' ' && cells[i] != word[i]) ok1 = false;
                if (cells[i] != ' ' && cells[i] != word[L - 1 - i]) ok2 = false;
            }
            return ok1 || ok2;
        }
        for (int r = 0; r < m; r++) {
            int c = 0;
            while (c < n) {
                while (c < n && board[r][c] == '#') c++;
                int start = c;
                while (c < n && board[r][c] != '#') c++;
                if (c - start == L) {
                    var sb = new StringBuilder();
                    for (int i = start; i < c; i++) sb.Append(board[r][i]);
                    if (Match(sb.ToString())) return true;
                }
            }
        }
        for (int c = 0; c < n; c++) {
            int r = 0;
            while (r < m) {
                while (r < m && board[r][c] == '#') r++;
                int start = r;
                while (r < m && board[r][c] != '#') r++;
                if (r - start == L) {
                    var sb = new StringBuilder();
                    for (int i = 0; i < L; i++) sb.Append(board[start + i][c]);
                    if (Match(sb.ToString())) return true;
                }
            }
        }
        return false;
    }
}
