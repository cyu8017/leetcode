// LeetCode 1958 - Check if Move is Legal
// https://leetcode.com/problems/check-if-move-is-legal/

public class Solution {
    public bool CheckMove(char[][] board, int rMove, int cMove, char color) {
        char opp = color == 'B' ? 'W' : 'B';
        int[][] dirs = { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1}, new[]{1,1}, new[]{1,-1}, new[]{-1,1}, new[]{-1,-1} };
        foreach (var d in dirs) {
            int r = rMove + d[0], c = cMove + d[1], steps = 0;
            while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == opp) {
                r += d[0]; c += d[1]; steps++;
            }
            if (steps > 0 && r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] == color) return true;
        }
        return false;
    }
}