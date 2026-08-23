// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

#include <vector>
#include <algorithm>

class BookMyShow {
    int n, m;
    struct Node { long long sum = 0, mx = 0; };
    std::vector<Node> tree;

    void pull(int idx) {
        tree[idx].sum = tree[idx * 2].sum + tree[idx * 2 + 1].sum;
        tree[idx].mx = std::max(tree[idx * 2].mx, tree[idx * 2 + 1].mx);
    }

    void build(int idx, int l, int r) {
        if (l == r) { tree[idx] = {m, m}; return; }
        int mid = (l + r) / 2;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        pull(idx);
    }

    void update(int idx, int l, int r, int pos, long long val) {
        if (l == r) { tree[idx].sum = tree[idx].mx = val; return; }
        int mid = (l + r) / 2;
        if (pos <= mid) update(idx * 2, l, mid, pos, val);
        else update(idx * 2 + 1, mid + 1, r, pos, val);
        pull(idx);
    }

    long long querySum(int idx, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return tree[idx].sum;
        int mid = (l + r) / 2;
        return querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr);
    }

    int findFirst(int idx, int l, int r, int maxRow, long long k) {
        if (l > maxRow || tree[idx].mx < k) return -1;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int left = findFirst(idx * 2, l, mid, maxRow, k);
        if (left != -1) return left;
        return findFirst(idx * 2 + 1, mid + 1, r, maxRow, k);
    }
public:
    BookMyShow(int n, int m) : n(n), m(m), tree(4 * n) {
        build(1, 0, n - 1);
    }

    std::vector<int> gather(int k, int maxRow) {
        int row = findFirst(1, 0, n - 1, maxRow, k);
        if (row == -1) return {};
        long long remain = querySum(1, 0, n - 1, row, row);
        int seat = (int)(m - remain);
        update(1, 0, n - 1, row, remain - k);
        return {row, seat};
    }

    bool scatter(int k, int maxRow) {
        if (querySum(1, 0, n - 1, 0, maxRow) < k) return false;
        long long need = k;
        for (int row = 0; row <= maxRow && need > 0; ++row) {
            long long remain = querySum(1, 0, n - 1, row, row);
            if (remain == 0) continue;
            long long take = std::min(remain, need);
            update(1, 0, n - 1, row, remain - take);
            need -= take;
        }
        return true;
    }
};
