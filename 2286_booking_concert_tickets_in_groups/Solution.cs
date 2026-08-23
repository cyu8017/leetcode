// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

using System;

public class BookMyShow {
    int n, m;
    struct Node { public long sum, mx; }
    Node[] tree;

    void Pull(int idx) {
        tree[idx].sum = tree[idx * 2].sum + tree[idx * 2 + 1].sum;
        tree[idx].mx = Math.Max(tree[idx * 2].mx, tree[idx * 2 + 1].mx);
    }

    void Build(int idx, int l, int r) {
        if (l == r) { tree[idx] = new Node { sum = m, mx = m }; return; }
        int mid = (l + r) / 2;
        Build(idx * 2, l, mid);
        Build(idx * 2 + 1, mid + 1, r);
        Pull(idx);
    }

    void Update(int idx, int l, int r, int pos, long val) {
        if (l == r) { tree[idx].sum = tree[idx].mx = val; return; }
        int mid = (l + r) / 2;
        if (pos <= mid) Update(idx * 2, l, mid, pos, val);
        else Update(idx * 2 + 1, mid + 1, r, pos, val);
        Pull(idx);
    }

    long QuerySum(int idx, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[idx].sum;
        int mid = (l + r) / 2;
        return QuerySum(idx * 2, l, mid, ql, qr) + QuerySum(idx * 2 + 1, mid + 1, r, ql, qr);
    }

    int FindFirst(int idx, int l, int r, int maxRow, long k) {
        if (l > maxRow || tree[idx].mx < k) return -1;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int left = FindFirst(idx * 2, l, mid, maxRow, k);
        if (left != -1) return left;
        return FindFirst(idx * 2 + 1, mid + 1, r, maxRow, k);
    }

    public BookMyShow(int n, int m) {
        this.n = n; this.m = m;
        tree = new Node[4 * n];
        Build(1, 0, n - 1);
    }

    public int[] Gather(int k, int maxRow) {
        int row = FindFirst(1, 0, n - 1, maxRow, k);
        if (row == -1) return new int[0];
        long remain = QuerySum(1, 0, n - 1, row, row);
        int seat = (int)(m - remain);
        Update(1, 0, n - 1, row, remain - k);
        return new int[] { row, seat };
    }

    public bool Scatter(int k, int maxRow) {
        if (QuerySum(1, 0, n - 1, 0, maxRow) < k) return false;
        long need = k;
        for (int row = 0; row <= maxRow && need > 0; row++) {
            long remain = QuerySum(1, 0, n - 1, row, row);
            if (remain == 0) continue;
            long take = Math.Min(remain, need);
            Update(1, 0, n - 1, row, remain - take);
            need -= take;
        }
        return true;
    }
}
