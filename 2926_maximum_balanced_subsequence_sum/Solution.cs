// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxBalancedSubsequenceSum(int[] nums) {
        int n = nums.Length;
        int[] keys = new int[n];
        for (int i = 0; i < n; i++) keys[i] = nums[i] - i;
        var uniq = new List<int>(keys);
        uniq.Sort();
        int w = 0;
        for (int i = 0; i < uniq.Count; i++)
            if (w == 0 || uniq[i] != uniq[w - 1]) uniq[w++] = uniq[i];
        while (uniq.Count > w) uniq.RemoveAt(uniq.Count - 1);

        int IdxOf(int v) {
            int lo = 0, hi = uniq.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (uniq[mid] < v) lo = mid + 1;
                else hi = mid;
            }
            return lo + 1;
        }

        const long negInf = -(1L << 60);
        long[] bit = new long[uniq.Count + 2];
        for (int i = 0; i < bit.Length; i++) bit[i] = negInf;

        void Update(int i, long val) {
            for (; i < bit.Length; i += i & -i)
                if (val > bit[i]) bit[i] = val;
        }
        long Query(int i) {
            long best = negInf;
            for (; i > 0; i -= i & -i)
                if (bit[i] > best) best = bit[i];
            return best;
        }

        long ans = negInf;
        for (int i = 0; i < n; i++) {
            int id = IdxOf(keys[i]);
            long best = Query(id);
            long cur = nums[i];
            if (best > negInf / 2) {
                long cand = best + nums[i];
                if (cand > cur) cur = cand;
            }
            Update(id, cur);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
