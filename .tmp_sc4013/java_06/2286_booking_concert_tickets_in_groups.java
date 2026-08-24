// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow {
    private int n, m;
    private long[] sum, mx;

    private void pull(int idx) {
        sum[idx] = sum[idx * 2] + sum[idx * 2 + 1];
        mx[idx] = Math.max(mx[idx * 2], mx[idx * 2 + 1]);
    }

    private void build(int idx, int l, int r) {
        if (l == r) {
            sum[idx] = mx[idx] = m;
            return;
        }
        int mid = (l + r) / 2;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        pull(idx);
    }

    private void update(int idx, int l, int r, int pos, long val) {
        if (l == r) {
            sum[idx] = mx[idx] = val;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(idx * 2, l, mid, pos, val);
        else update(idx * 2 + 1, mid + 1, r, pos, val);
        pull(idx);
    }

    private long querySum(int idx, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 0;
        if (ql <= l && r <= qr) return sum[idx];
        int mid = (l + r) / 2;
        return querySum(idx * 2, l, mid, ql, qr) + querySum(idx * 2 + 1, mid + 1, r, ql, qr);
    }

    private int findFirst(int idx, int l, int r, int maxRow, long k) {
        if (l > maxRow || mx[idx] < k) return -1;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int left = findFirst(idx * 2, l, mid, maxRow, k);
        if (left != -1) return left;
        return findFirst(idx * 2 + 1, mid + 1, r, maxRow, k);
    }

    public BookMyShow(int n, int m) {
        this.n = n;
        this.m = m;
        sum = new long[4 * n];
        mx = new long[4 * n];
        build(1, 0, n - 1);
    }

    public int[] gather(int k, int maxRow) {
        int row = findFirst(1, 0, n - 1, maxRow, k);
        if (row == -1) return new int[0];
        long remain = querySum(1, 0, n - 1, row, row);
        int seat = (int) (m - remain);
        update(1, 0, n - 1, row, remain - k);
        return new int[] { row, seat };
    }

    public boolean scatter(int k, int maxRow) {
        if (querySum(1, 0, n - 1, 0, maxRow) < k) return false;
        long need = k;
        for (int row = 0; row <= maxRow && need > 0; row++) {
            long remain = querySum(1, 0, n - 1, row, row);
            if (remain == 0) continue;
            long take = Math.min(remain, need);
            update(1, 0, n - 1, row, remain - take);
            need -= take;
        }
        return true;
    }
}
