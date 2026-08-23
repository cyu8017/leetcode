// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

using System;
using System.Collections.Generic;

public class Solution {
    private class Fenwick {
        private int[] bit;
        public Fenwick(int n) { bit = new int[n + 2]; }
        public void Add(int i, int v) {
            for (; i < bit.Length; i += i & -i) bit[i] += v;
        }
        public int Sum(int i) {
            int s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        }
    }

    public int KBigIndices(int[] nums, int k) {
        int n = nums.Length;
        int[] uniq = (int[])nums.Clone();
        Array.Sort(uniq);
        int m = 0;
        for (int i = 0; i < uniq.Length; i++) {
            if (i == 0 || uniq[i] != uniq[i - 1]) uniq[m++] = uniq[i];
        }
        var rank = new Dictionary<int, int>();
        for (int i = 0; i < m; i++) rank[uniq[i]] = i + 1;
        int[] left = new int[n], right = new int[n];
        var ft = new Fenwick(m);
        for (int i = 0; i < n; i++) {
            int r = rank[nums[i]];
            left[i] = ft.Sum(r - 1);
            ft.Add(r, 1);
        }
        ft = new Fenwick(m);
        for (int i = n - 1; i >= 0; i--) {
            int r = rank[nums[i]];
            right[i] = ft.Sum(r - 1);
            ft.Add(r, 1);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (left[i] >= k && right[i] >= k) ans++;
        }
        return ans;
    }
}
