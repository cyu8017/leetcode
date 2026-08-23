// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

import java.util.Arrays;

class Solution {
    public long[] maximumCoins(int[] heroes, int[] monsters, int[] coins) {
        int n = monsters.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(monsters[a], monsters[b]));
        long[] pref = new long[n + 1];
        int[] ms = new int[n];
        for (int i = 0; i < n; i++) {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]];
        }
        long[] ans = new long[heroes.length];
        for (int i = 0; i < heroes.length; i++) {
            int p = upperBound(ms, heroes[i]);
            ans[i] = pref[p];
        }
        return ans;
    }

    private int upperBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
