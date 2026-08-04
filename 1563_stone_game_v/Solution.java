// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

import java.util.*;

class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        if (n == 0) {
            return 0;
        }
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pre[i + 1] = pre[i] + stoneValue[i];
        }
        int[][] dp = new int[n][n];
        int[][] left = new int[n][n];
        int[][] right = new int[n][n];
        for (int i = 0; i < n; i++) {
            left[i][i] = stoneValue[i];
            right[i][i] = stoneValue[i];
        }
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                int lo = i;
                int hi = j - 1;
                while (lo <= hi) {
                    int mid = (lo + hi) >>> 1;
                    if (2L * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]) {
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }
                int split = lo;
                int leftSum = pre[split + 1] - pre[i];
                int rightSum = pre[j + 1] - pre[split + 1];
                int best = right[split + 1][j];
                if (leftSum == rightSum) {
                    best = Math.max(best, left[i][split]);
                } else if (split > i) {
                    best = Math.max(best, left[i][split - 1]);
                }
                dp[i][j] = best;
                int total = pre[j + 1] - pre[i];
                left[i][j] = Math.max(left[i][j - 1], total + best);
                right[i][j] = Math.max(right[i + 1][j], total + best);
            }
        }
        return dp[0][n - 1];
    }
}
