// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

class Solution {
    public String lexicographicallySmallestString(String s) {
        int n = s.length();
        String[][] dp = new String[n + 1][n + 1];
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= n; j++) dp[i][j] = "";
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i + length <= n; i++) {
                int j = i + length;
                String minStr = s.charAt(i) + dp[i + 1][j];
                for (int k = i + 1; k < j; k++) {
                    if (isConsec(s.charAt(i), s.charAt(k)) && dp[i + 1][k].isEmpty()) {
                        String cand = dp[k + 1][j];
                        if (cand.compareTo(minStr) < 0) minStr = cand;
                    }
                }
                dp[i][j] = minStr;
            }
        }
        return dp[0][n];
    }

    boolean isConsec(char a, char b) {
        int d = Math.abs(a - b);
        return d == 1 || d == 25;
    }
}
