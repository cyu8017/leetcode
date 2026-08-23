// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[] nums1;
    private int[] ones;
    private boolean[] lazy;

    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        this.nums1 = nums1;
        int n = nums1.length;
        ones = new int[4 * n];
        lazy = new boolean[4 * n];
        build(1, 0, n - 1);
        long sum2 = 0;
        for (int x : nums2) sum2 += x;
        List<Long> ans = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) update(1, 0, n - 1, q[1], q[2]);
            else if (q[0] == 2) sum2 += (long) q[1] * ones[1];
            else ans.add(sum2);
        }
        long[] res = new long[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }

    private void build(int idx, int l, int r) {
        if (l == r) {
            ones[idx] = nums1[l];
            return;
        }
        int m = (l + r) / 2;
        build(idx * 2, l, m);
        build(idx * 2 + 1, m + 1, r);
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
    }

    private void apply(int idx, int l, int r) {
        ones[idx] = (r - l + 1) - ones[idx];
        lazy[idx] = !lazy[idx];
    }

    private void push(int idx, int l, int r) {
        if (lazy[idx] && l != r) {
            int m = (l + r) / 2;
            apply(idx * 2, l, m);
            apply(idx * 2 + 1, m + 1, r);
            lazy[idx] = false;
        }
    }

    private void update(int idx, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            apply(idx, l, r);
            return;
        }
        push(idx, l, r);
        int m = (l + r) / 2;
        if (ql <= m) update(idx * 2, l, m, ql, qr);
        if (qr > m) update(idx * 2 + 1, m + 1, r, ql, qr);
        ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
    }
}
