// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

class Solution {
    static class Node {
        int l, r;
        int s00, s01, s10, s11;
    }

    private Node[] tr;

    private void build(int u, int l, int r) {
        tr[u].l = l;
        tr[u].r = r;
        if (l == r) return;
        int mid = (l + r) >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
    }

    private void pushup(int u) {
        Node left = tr[u << 1];
        Node right = tr[u << 1 | 1];
        tr[u].s00 = Math.max(left.s00 + right.s10, left.s01 + right.s00);
        tr[u].s01 = Math.max(left.s00 + right.s11, left.s01 + right.s01);
        tr[u].s10 = Math.max(left.s10 + right.s10, left.s11 + right.s00);
        tr[u].s11 = Math.max(left.s10 + right.s11, left.s11 + right.s01);
    }

    private void modify(int u, int x, int v) {
        if (tr[u].l == tr[u].r) {
            tr[u].s11 = Math.max(0, v);
            return;
        }
        int mid = (tr[u].l + tr[u].r) >> 1;
        if (x <= mid) modify(u << 1, x, v);
        else modify(u << 1 | 1, x, v);
        pushup(u);
    }

    private int query(int u, int l, int r) {
        if (tr[u].l >= l && tr[u].r <= r) return tr[u].s11;
        int mid = (tr[u].l + tr[u].r) >> 1;
        int ans = 0;
        if (r <= mid) ans = query(u << 1, l, r);
        if (l > mid) ans = Math.max(ans, query(u << 1 | 1, l, r));
        return ans;
    }

    public int maximumSumSubsequence(int[] nums, int[][] queries) {
        int n = nums.length;
        tr = new Node[n * 4];
        for (int i = 0; i < tr.length; i++) tr[i] = new Node();
        build(1, 1, n);
        for (int i = 0; i < n; i++) modify(1, i + 1, nums[i]);
        final int MOD = 1_000_000_007;
        int ans = 0;
        for (int[] q : queries) {
            modify(1, q[0] + 1, q[1]);
            ans = (ans + query(1, 1, n)) % MOD;
        }
        return ans;
    }
}
