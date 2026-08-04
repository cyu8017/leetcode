// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution {
    int m;
    int[][] score;
    Integer[] memo;

    public int maxCompatibilitySum(int[][] students, int[][] mentors) {
        m = students.length;
        score = new int[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                int s = 0;
                for (int k = 0; k < students[i].length; k++) if (students[i][k] == mentors[j][k]) s++;
                score[i][j] = s;
            }
        }
        memo = new Integer[1 << m];
        return dp(0, 0);
    }

    private int dp(int i, int mask) {
        if (i == m) return 0;
        if (memo[mask] != null) return memo[mask];
        int best = 0;
        for (int j = 0; j < m; j++) {
            if ((mask & (1 << j)) == 0) best = Math.max(best, score[i][j] + dp(i + 1, mask | (1 << j)));
        }
        return memo[mask] = best;
    }
}
