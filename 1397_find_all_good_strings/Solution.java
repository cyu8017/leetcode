// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

class Solution {
    private static final int MOD = 1_000_000_007;
    private int n, m;
    private String s1, s2;
    private int[][] trans;
    private Integer[][][][] memo;

    public int findGoodStrings(int n, String s1, String s2, String evil) {
        this.n = n;
        this.s1 = s1;
        this.s2 = s2;
        m = evil.length();
        int[] pi = new int[m];
        for (int i = 1; i < m; i++) {
            int j = pi[i - 1];
            while (j > 0 && evil.charAt(i) != evil.charAt(j)) j = pi[j - 1];
            if (evil.charAt(i) == evil.charAt(j)) j++;
            pi[i] = j;
        }
        trans = new int[m][26];
        for (int j = 0; j < m; j++) {
            for (int x = 0; x < 26; x++) {
                char c = (char) ('a' + x);
                int k = j;
                while (k > 0 && evil.charAt(k) != c) k = pi[k - 1];
                if (evil.charAt(k) == c) k++;
                trans[j][x] = k;
            }
        }
        memo = new Integer[n + 1][m + 1][2][2];
        return dp(0, 0, 1, 1);
    }

    private int dp(int i, int j, int lo, int hi) {
        if (j == m) return 0;
        if (i == n) return 1;
        if (memo[i][j][lo][hi] != null) return memo[i][j][lo][hi];
        int a = lo == 1 ? s1.charAt(i) - 'a' : 0;
        int b = hi == 1 ? s2.charAt(i) - 'a' : 25;
        long ans = 0;
        for (int x = a; x <= b; x++) {
            ans += dp(i + 1, trans[j][x], lo == 1 && x == a ? 1 : 0, hi == 1 && x == b ? 1 : 0);
        }
        return memo[i][j][lo][hi] = (int) (ans % MOD);
    }
}
