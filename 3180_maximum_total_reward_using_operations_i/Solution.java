// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

import java.util.Arrays;

class Solution {
    private int[] rewardValues;
    private int[] f;
    private int n;

    public int maxTotalReward(int[] rewardValues) {
        Arrays.sort(rewardValues);
        this.rewardValues = rewardValues;
        n = rewardValues.length;
        f = new int[rewardValues[n - 1] << 1];
        Arrays.fill(f, -1);
        return dfs(0);
    }

    private int dfs(int x) {
        if (f[x] != -1) {
            return f[x];
        }
        int idx = upperBound(rewardValues, x);
        f[x] = 0;
        for (int it = idx; it < n; it++) {
            f[x] = Math.max(f[x], rewardValues[it] + dfs(x + rewardValues[it]));
        }
        return f[x];
    }

    private static int upperBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
