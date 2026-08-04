// LeetCode 1340 - Jump Game V
// https://leetcode.com/problems/jump-game-v/

import java.util.*;

class Solution {
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> arr[i]));
        for (int i : order) {
            for (int step : new int[]{-1, 1}) {
                int j = i + step;
                while (j >= 0 && j < n && Math.abs(j - i) <= d && arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], 1 + dp[j]);
                    j += step;
                }
            }
        }
        int ans = 0;
        for (int v : dp) ans = Math.max(ans, v);
        return ans;
    }
}
