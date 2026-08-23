// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution {
    public int countWinningSequences(String s) {
        final int mod = 1000000007;
        int n = s.length();
        int[] mp = new int[256];
        mp['F'] = 0; mp['W'] = 1; mp['E'] = 2;
        int[] beat = new int[] { 2, 0, 1 };
        int[][] score = new int[3][];
        for (int a = 0; a < 3; a++) {
            score[a] = new int[3];
            for (int b = 0; b < 3; b++) {
                if (a == b) score[a][b] = 0;
                else if (beat[a] == b) score[a][b] = 1;
                else score[a][b] = -1;
            }
        }
        int offset = n;
        int[][] dp = new int[3][];
        for (int a = 0; a < 3; a++) dp[a] = new int[2 * n + 1];
        int b0 = mp[s.charAt(0)];
        for (int a = 0; a < 3; a++) dp[a][score[a][b0] + offset] = 1;
        for (int i = 1; i < n; i++) {
            int[][] ndp = new int[3][];
            for (int a = 0; a < 3; a++) ndp[a] = new int[2 * n + 1];
            int b = mp[s.charAt(i)];
            for (int last = 0; last < 3; last++) {
                for (int d = 0; d <= 2 * n; d++) {
                    if (dp[last][d] == 0) continue;
                    for (int a = 0; a < 3; a++) {
                        if (a == last) continue;
                        int nd = d + score[a][b];
                        if (nd < 0 || nd > 2 * n) continue;
                        ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod;
                    }
                }
            }
            dp = ndp;
        }
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            for (int d = offset + 1; d <= 2 * n; d++) ans = (ans + dp[a][d]) % mod;
        }
        return ans;
    }
}
