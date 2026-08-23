// LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

using System;

public class Solution {
    public long MinInversionCount(int[] nums, int k) {
        int[] vals = (int[])nums.Clone();
        Array.Sort(vals);
        int vu = 0;
        for (int i = 0; i < vals.Length; i++) {
            if (i == 0 || vals[i] != vals[i - 1]) vals[vu++] = vals[i];
        }
        Array.Resize(ref vals, vu);
        int[] bit = new int[vals.Length + 1];
        void Add(int i, int delta) {
            for (; i < bit.Length; i += i & -i) bit[i] += delta;
        }
        int Sum(int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
        int[] rank = new int[nums.Length];
        long inv = 0;
        for (int i = 0; i < nums.Length; i++) {
            rank[i] = LowerBound(vals, nums[i]) + 1;
            if (i < k) {
                inv += i - Sum(rank[i]);
                Add(rank[i], 1);
            }
        }
        long best = inv;
        for (int r = k; r < nums.Length; r++) {
            int left = rank[r - k];
            inv -= Sum(left - 1);
            Add(left, -1);
            inv += k - 1 - Sum(rank[r]);
            Add(rank[r], 1);
            if (inv < best) best = inv;
        }
        return best;
    }

    static int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
