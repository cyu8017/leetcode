// LeetCode 1301 - Number Of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

import java.util.*;

class Solution {
    public int[] pathsWithMaxScore(List<String> board) {
        int mod = 1_000_000_007, n = board.size();
        int[][] score = new int[n][n];
        int[][] ways = new int[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(score[i], -1);
        score[n - 1][n - 1] = 0;
        ways[n - 1][n - 1] = 1;
        int[][] dirs = {{1, 0}, {0, 1}, {1, 1}};
        for (int r = n - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (board.get(r).charAt(c) == 'X' || (r == n - 1 && c == n - 1)) continue;
                int best = -1, count = 0;
                for (int[] d : dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr < n && nc < n && score[nr][nc] >= 0) {
                        if (score[nr][nc] > best) {
                            best = score[nr][nc];
                            count = ways[nr][nc];
                        } else if (score[nr][nc] == best) {
                            count = (count + ways[nr][nc]) % mod;
                        }
                    }
                }
                if (best >= 0) {
                    char ch = board.get(r).charAt(c);
                    score[r][c] = best + (ch >= '0' && ch <= '9' ? ch - '0' : 0);
                    ways[r][c] = count;
                }
            }
        }
        return new int[]{Math.max(score[0][0], 0), ways[0][0]};
    }
}
