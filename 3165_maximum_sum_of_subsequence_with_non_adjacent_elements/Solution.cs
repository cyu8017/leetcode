// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

using System;

public class Solution {
    class Node {
        public int l, r;
        public int s00, s01, s10, s11;
    }
    Node[] tr;

    void Build(int u, int l, int r) {
        tr[u].l = l; tr[u].r = r;
        if (l == r) return;
        int mid = (l + r) >> 1;
        Build(u << 1, l, mid);
        Build(u << 1 | 1, mid + 1, r);
    }

    void Pushup(int u) {
        Node left = tr[u << 1];
        Node right = tr[u << 1 | 1];
        tr[u].s00 = Math.Max(left.s00 + right.s10, left.s01 + right.s00);
        tr[u].s01 = Math.Max(left.s00 + right.s11, left.s01 + right.s01);
        tr[u].s10 = Math.Max(left.s10 + right.s10, left.s11 + right.s00);
        tr[u].s11 = Math.Max(left.s10 + right.s11, left.s11 + right.s01);
    }

    void Modify(int u, int x, int v) {
        if (tr[u].l == tr[u].r) {
            tr[u].s11 = Math.Max(0, v);
            return;
        }
        int mid = (tr[u].l + tr[u].r) >> 1;
        if (x <= mid) Modify(u << 1, x, v);
        else Modify(u << 1 | 1, x, v);
        Pushup(u);
    }

    int Query(int u, int l, int r) {
        if (tr[u].l >= l && tr[u].r <= r) return tr[u].s11;
        int mid = (tr[u].l + tr[u].r) >> 1;
        int ans = 0;
        if (r <= mid) ans = Query(u << 1, l, r);
        if (l > mid) ans = Math.Max(ans, Query(u << 1 | 1, l, r));
        return ans;
    }

    public int MaximumSumSubsequence(int[] nums, int[][] queries) {
        int n = nums.Length;
        tr = new Node[n * 4];
        for (int i = 0; i < tr.Length; i++) tr[i] = new Node();
        Build(1, 1, n);
        for (int i = 0; i < n; i++) Modify(1, i + 1, nums[i]);
        const int Mod = 1000000007;
        int ans = 0;
        foreach (var q in queries) {
            Modify(1, q[0] + 1, q[1]);
            ans = (ans + Query(1, 1, n)) % Mod;
        }
        return ans;
    }
}
