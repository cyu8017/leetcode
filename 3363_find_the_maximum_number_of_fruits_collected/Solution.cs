// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

public class Solution {
    public int MaxCollectedFruits(int[][] fruits) {
        int n = fruits.Length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += fruits[i][i];
            fruits[i][i] = 0;
        }
        const int neg = -(1 << 30);
        int[][] dp2 = new int[n][];
        int[][] dp3 = new int[n][];
        for (int i = 0; i < n; i++) {
            dp2[i] = new int[n];
            dp3[i] = new int[n];
            for (int j = 0; j < n; j++) { dp2[i][j] = neg; dp3[i][j] = neg; }
        }
        dp2[0][n - 1] = fruits[0][n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp2[i][j] == neg) continue;
                foreach (int dj in new int[] { -1, 0, 1 }) {
                    int ni = i + 1, nj = j + dj;
                    if (ni < n && nj >= 0 && nj < n && nj > ni) {
                        int v = dp2[i][j] + fruits[ni][nj];
                        if (v > dp2[ni][nj]) dp2[ni][nj] = v;
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                if (dp3[i][j] == neg) continue;
                foreach (int di in new int[] { -1, 0, 1 }) {
                    int ni = i + di, nj = j + 1;
                    if (ni >= 0 && ni < n && nj < n && ni > nj) {
                        int v = dp3[i][j] + fruits[ni][nj];
                        if (v > dp3[ni][nj]) dp3[ni][nj] = v;
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1];
        return ans;
    }
}
