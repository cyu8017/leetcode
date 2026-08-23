// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

using System;
using System.Collections.Generic;

public class Solution {
    class Node {
        public int L, R, Mn, Mx, Lazy;
    }

    class SegmentTree {
        Node[] tr;
        public SegmentTree(int n) {
            tr = new Node[n << 2];
            for (int i = 0; i < tr.Length; i++) tr[i] = new Node();
            Build(1, 0, n);
        }
        void Build(int u, int l, int r) {
            tr[u].L = l; tr[u].R = r; tr[u].Mn = tr[u].Mx = tr[u].Lazy = 0;
            if (l == r) return;
            int mid = (l + r) >> 1;
            Build(u << 1, l, mid);
            Build(u << 1 | 1, mid + 1, r);
        }
        void Apply(int u, int v) {
            tr[u].Mn += v;
            tr[u].Mx += v;
            tr[u].Lazy += v;
        }
        void Pushup(int u) {
            tr[u].Mn = Math.Min(tr[u << 1].Mn, tr[u << 1 | 1].Mn);
            tr[u].Mx = Math.Max(tr[u << 1].Mx, tr[u << 1 | 1].Mx);
        }
        void Pushdown(int u) {
            if (tr[u].Lazy != 0) {
                int v = tr[u].Lazy;
                Apply(u << 1, v);
                Apply(u << 1 | 1, v);
                tr[u].Lazy = 0;
            }
        }
        public void Modify(int u, int l, int r, int v) {
            if (tr[u].L >= l && tr[u].R <= r) {
                Apply(u, v);
                return;
            }
            Pushdown(u);
            int mid = (tr[u].L + tr[u].R) >> 1;
            if (l <= mid) Modify(u << 1, l, r, v);
            if (r > mid) Modify(u << 1 | 1, l, r, v);
            Pushup(u);
        }
        public int Query(int u, int target) {
            if (tr[u].L == tr[u].R) return tr[u].L;
            Pushdown(u);
            int left = u << 1, right = u << 1 | 1;
            if (tr[left].Mn <= target && target <= tr[left].Mx) return Query(left, target);
            return Query(right, target);
        }
    }

    public int LongestBalanced(int[] nums) {
        int n = nums.Length;
        var st = new SegmentTree(n);
        var last = new Dictionary<int, int>();
        int now = 0, ans = 0;
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int det = (x & 1) != 0 ? 1 : -1;
            if (last.ContainsKey(x)) {
                st.Modify(1, last[x], n, -det);
                now -= det;
            }
            last[x] = i;
            st.Modify(1, i, n, det);
            now += det;
            int pos = st.Query(1, now);
            ans = Math.Max(ans, i - pos);
        }
        return ans;
    }
}
