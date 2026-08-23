// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

using System;

public class Solution {
    public long MinMoves(int[] balance) {
        long sum = 0;
        foreach (int b in balance) sum += b;
        if (sum < 0) return -1;

        int n = balance.Length;
        int mn = balance[0], idx = 0;
        for (int i = 1; i < n; i++) {
            if (balance[i] < mn) {
                mn = balance[i];
                idx = i;
            }
        }
        if (mn >= 0) return 0;

        int need = -mn;
        long ans = 0;
        for (int j = 1; j < n; j++) {
            int a = balance[(idx - j + n) % n];
            int b = balance[(idx + j) % n];
            int c1 = Math.Min(a, need);
            need -= c1;
            ans += (long)c1 * j;
            int c2 = Math.Min(b, need);
            need -= c2;
            ans += (long)c2 * j;
        }
        return ans;
    }
}
