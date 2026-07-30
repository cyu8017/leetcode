// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

using System;

public class Solution {
    public int StoneGameV(int[] stoneValue) {
        int n = stoneValue.Length;
        if (n == 0) return 0;
        int[] pre = new int[n + 1];
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + stoneValue[i];
        int[,] dp = new int[n, n];
        int[,] left = new int[n, n];
        int[,] right = new int[n, n];
        for (int i = 0; i < n; i++) left[i, i] = right[i, i] = stoneValue[i];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i + length - 1 < n; i++) {
                int j = i + length - 1;
                int lo = i, hi = j - 1;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]) hi = mid - 1;
                    else lo = mid + 1;
                }
                int split = lo;
                int leftSum = pre[split + 1] - pre[i];
                int rightSum = pre[j + 1] - pre[split + 1];
                int best = right[split + 1, j];
                if (leftSum == rightSum) best = Math.Max(best, left[i, split]);
                else if (split > i) best = Math.Max(best, left[i, split - 1]);
                dp[i, j] = best;
                int total = pre[j + 1] - pre[i];
                left[i, j] = Math.Max(left[i, j - 1], total + best);
                right[i, j] = Math.Max(right[i + 1, j], total + best);
            }
        }
        return dp[0, n - 1];
    }
}
