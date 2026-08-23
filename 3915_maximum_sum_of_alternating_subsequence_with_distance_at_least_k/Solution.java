// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

import java.util.Arrays;

class Solution {
    static class Fenwick {
        long[] f;
        Fenwick(int n) { f = new long[n]; }
        void update(int i, long val) {
            for (; i < f.length; i += i & -i) f[i] = Math.max(f[i], val);
        }
        long preMax(int i) {
            long res = 0;
            for (; i > 0; i &= i - 1) res = Math.max(res, f[i]);
            return res;
        }
    }

    public long maxAlternatingSum(int[] nums, int k) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int m = 0;
        for (int i = 0; i < sorted.length; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) sorted[m++] = sorted[i];
        }
        sorted = Arrays.copyOf(sorted, m);
        int n = nums.length;
        long[] fInc = new long[n];
        long[] fDec = new long[n];
        Fenwick inc = new Fenwick(m + 1);
        Fenwick dec = new Fenwick(m + 1);
        long ans = 0;
        int[] ranks = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (i >= k) {
                int j = ranks[i - k];
                inc.update(m - j, fInc[i - k]);
                dec.update(j + 1, fDec[i - k]);
            }
            int jr = Arrays.binarySearch(sorted, x);
            if (jr < 0) jr = ~jr;
            ranks[i] = jr;
            fInc[i] = dec.preMax(jr) + x;
            fDec[i] = inc.preMax(m - 1 - jr) + x;
            ans = Math.max(ans, Math.max(fInc[i], fDec[i]));
        }
        return ans;
    }
}
