// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

using System;

public class Solution {
    public long MinTotalTime(int[] forward, int[] backward, int[] queries) {
        int n = forward.Length;
        int sumB = 0;
        foreach (int v in backward) sumB += v;
        int[] pf = new int[n + 1], pb = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pf[i + 1] = pf[i] + forward[i];
            pb[i + 1] = pb[i] + backward[i];
        }
        long ans = 0;
        int pos = 0;
        foreach (int q in queries) {
            int r = 0;
            if (q < pos) r = pf[n];
            r += pf[q] - pf[pos];
            int l = 0;
            if (q > pos) l = sumB;
            l += pb[pos] - pb[q];
            ans += Math.Min(l, r);
            pos = q;
        }
        return ans;
    }
}
