// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

using System;

public class Solution {
    public int MaxScore(int n, int k, int[][] stayScore, int[][] travelScore) {
        int[] dp = new int[n];
        for (int day = 0; day < k; day++) {
            int[] ndp = new int[n];
            for (int i = 0; i < n; i++) ndp[i] = -(1 << 30);
            for (int dest = 0; dest < n; dest++) {
                int best = -(1 << 30);
                for (int src = 0; src < n; src++) {
                    int val = dp[src];
                    if (src == dest) val += stayScore[day][dest];
                    else val += travelScore[src][dest];
                    if (val > best) best = val;
                }
                ndp[dest] = best;
            }
            dp = ndp;
        }
        int ans = dp[0];
        for (int i = 1; i < n; i++) if (dp[i] > ans) ans = dp[i];
        return ans;
    }
}
