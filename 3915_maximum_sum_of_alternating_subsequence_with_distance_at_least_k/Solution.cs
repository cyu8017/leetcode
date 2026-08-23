// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

using System;

public class Solution {
    class Fenwick {
        long[] f;
        public Fenwick(int n) { f = new long[n]; }
        public void Update(int i, long val) {
            for (; i < f.Length; i += i & -i) f[i] = Math.Max(f[i], val);
        }
        public long PreMax(int i) {
            long res = 0;
            for (; i > 0; i &= i - 1) res = Math.Max(res, f[i]);
            return res;
        }
    }

    public long MaxAlternatingSum(int[] nums, int k) {
        var sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        int m = 0;
        for (int i = 0; i < sorted.Length; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
        }
        Array.Resize(ref sorted, m);
        int n = nums.Length;
        var fInc = new long[n];
        var fDec = new long[n];
        var inc = new Fenwick(m + 1);
        var dec = new Fenwick(m + 1);
        long ans = 0;
        var ranks = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (i >= k) {
                int j = ranks[i - k];
                inc.Update(m - j, fInc[i - k]);
                dec.Update(j + 1, fDec[i - k]);
            }
            int jr = Array.BinarySearch(sorted, x);
            if (jr < 0) jr = ~jr;
            ranks[i] = jr;
            fInc[i] = dec.PreMax(jr) + x;
            fDec[i] = inc.PreMax(m - 1 - jr) + x;
            ans = Math.Max(ans, Math.Max(fInc[i], fDec[i]));
        }
        return ans;
    }
}
