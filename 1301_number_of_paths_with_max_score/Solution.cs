// LeetCode 1301 - Number Of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

using System.Collections.Generic;

public class Solution {
    public int[] PathsWithMaxScore(IList<string> board) {
        int mod = 1000000007, n = board.Count;
        var score = new int[n, n];
        var ways = new int[n, n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                score[i, j] = -1;
        score[n - 1, n - 1] = 0;
        ways[n - 1, n - 1] = 1;
        for (int r = n - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (board[r][c] == 'X' || (r == n - 1 && c == n - 1)) continue;
                int best = -1, count = 0;
                foreach (var (nr, nc) in new[] { (r + 1, c), (r, c + 1), (r + 1, c + 1) }) {
                    if (nr < n && nc < n && score[nr, nc] >= 0) {
                        if (score[nr, nc] > best) { best = score[nr, nc]; count = ways[nr, nc]; }
                        else if (score[nr, nc] == best) count = (count + ways[nr, nc]) % mod;
                    }
                }
                if (best >= 0) {
                    char ch = board[r][c];
                    score[r, c] = best + (ch >= '0' && ch <= '9' ? ch - '0' : 0);
                    ways[r, c] = count;
                }
            }
        }
        return new[] { System.Math.Max(score[0, 0], 0), ways[0, 0] };
    }
}
