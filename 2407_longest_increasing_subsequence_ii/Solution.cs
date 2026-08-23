// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

using System;

public class Solution {
    public int LengthOfLIS(int[] nums, int k) {
        int maxV = 0;
        foreach (int x in nums) maxV = Math.Max(maxV, x);
        var st = new SegTree(maxV + 1);
        int ans = 0;
        foreach (int x in nums) {
            int lo = Math.Max(1, x - k);
            int best = 1;
            if (lo <= x - 1) best = st.Query(1, 1, maxV, lo, x - 1) + 1;
            st.Update(1, 1, maxV, x, best);
            ans = Math.Max(ans, best);
        }
        return ans;
    }

    private class SegTree {
        private readonly int[] tree;
        public SegTree(int n) { tree = new int[4 * n]; }
        public void Update(int idx, int l, int r, int pos, int val) {
            if (l == r) { tree[idx] = Math.Max(tree[idx], val); return; }
            int mid = (l + r) / 2;
            if (pos <= mid) Update(idx * 2, l, mid, pos, val);
            else Update(idx * 2 + 1, mid + 1, r, pos, val);
            tree[idx] = Math.Max(tree[idx * 2], tree[idx * 2 + 1]);
        }
        public int Query(int idx, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return 0;
            if (ql <= l && r <= qr) return tree[idx];
            int mid = (l + r) / 2;
            return Math.Max(Query(idx * 2, l, mid, ql, qr), Query(idx * 2 + 1, mid + 1, r, ql, qr));
        }
    }
}
