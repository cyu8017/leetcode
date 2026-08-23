// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

using System;

public class Solution {
    public long[] MaximumCoins(int[] heroes, int[] monsters, int[] coins) {
        int n = monsters.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => monsters[a].CompareTo(monsters[b]));
        long[] pref = new long[n + 1];
        int[] ms = new int[n];
        for (int i = 0; i < n; i++) {
            ms[i] = monsters[idx[i]];
            pref[i + 1] = pref[i] + coins[idx[i]];
        }
        long[] ans = new long[heroes.Length];
        for (int i = 0; i < heroes.Length; i++) {
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (ms[mid] <= heroes[i]) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = pref[lo];
        }
        return ans;
    }
}
