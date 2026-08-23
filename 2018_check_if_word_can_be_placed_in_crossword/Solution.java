// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution {
    public boolean placeWordInCrossword(char[][] board, String word) {
        int m = board.length, n = board[0].length, L = word.length();
        for (int r = 0; r < m; r++) {
            int c = 0;
            while (c < n) {
                while (c < n && board[r][c] == '#') c++;
                int start = c;
                while (c < n && board[r][c] != '#') c++;
                if (c - start == L) {
                    StringBuilder sb = new StringBuilder();
                    for (int i = start; i < c; i++) sb.append(board[r][i]);
                    if (match(sb.toString(), word)) return true;
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
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < L; i++) sb.append(board[start + i][c]);
                    if (match(sb.toString(), word)) return true;
                }
            }
        }
        return false;
    }

    private boolean match(String cells, String word) {
        int L = word.length();
        if (cells.length() != L) return false;
        boolean ok1 = true, ok2 = true;
        for (int i = 0; i < L; i++) {
            if (cells.charAt(i) != ' ' && cells.charAt(i) != word.charAt(i)) ok1 = false;
            if (cells.charAt(i) != ' ' && cells.charAt(i) != word.charAt(L - 1 - i)) ok2 = false;
        }
        return ok1 || ok2;
    }
}
