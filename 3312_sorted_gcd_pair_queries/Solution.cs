// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

using System;

public class Solution {
    public int[] GcdValues(int[] nums, long[] queries) {
        int maxV = 0;
        foreach (int x in nums) if (x > maxV) maxV = x;
        int[] cnt = new int[maxV + 1];
        foreach (int x in nums) cnt[x]++;
        long[] divCnt = new long[maxV + 1];
        for (int g = 1; g <= maxV; g++) {
            long c = 0;
            for (int m = g; m <= maxV; m += g) c += cnt[m];
            divCnt[g] = c * (c - 1) / 2;
        }
        long[] exact = new long[maxV + 1];
        for (int g = maxV; g >= 1; g--) {
            exact[g] = divCnt[g];
            for (int m = 2 * g; m <= maxV; m += g) exact[g] -= exact[m];
        }
        long[] pref = new long[maxV + 1];
        for (int g = 1; g <= maxV; g++) pref[g] = pref[g - 1] + exact[g];
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            long q = queries[i];
            int lo = 1, hi = maxV;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (pref[mid] > q) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = lo;
        }
        return ans;
    }
}
