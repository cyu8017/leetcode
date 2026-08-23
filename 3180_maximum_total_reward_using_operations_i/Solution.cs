// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

using System;

public class Solution {
    public int MaxTotalReward(int[] rewardValues) {
        Array.Sort(rewardValues);
        int n = rewardValues.Length;
        int[] f = new int[rewardValues[n - 1] << 1];
        Array.Fill(f, -1);
        int Dfs(int x) {
            if (f[x] != -1) return f[x];
            int idx = UpperBound(rewardValues, x);
            f[x] = 0;
            for (int it = idx; it < n; it++) {
                f[x] = Math.Max(f[x], rewardValues[it] + Dfs(x + rewardValues[it]));
            }
            return f[x];
        }
        return Dfs(0);
    }

    static int UpperBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
