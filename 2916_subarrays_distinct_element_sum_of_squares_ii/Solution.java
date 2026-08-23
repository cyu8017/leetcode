// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1000000007;
    private Node[] tree;

    private static class Node {
        int sum, sumSq, lazy;
    }

    public int sumCounts(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> last = new HashMap<>();
        tree = new Node[4 * (n + 2)];
        for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            int prev = last.getOrDefault(v, 0);
            update(1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sumSq) % MOD;
            last.put(v, i);
        }
        return ans;
    }

    private void apply(int idx, int l, int r, int val) {
        int length = r - l + 1;
        tree[idx].sumSq = (int) ((tree[idx].sumSq + 2L * val % MOD * tree[idx].sum % MOD
                + 1L * val % MOD * val % MOD * length % MOD) % MOD);
        tree[idx].sum = (int) ((tree[idx].sum + 1L * val % MOD * length % MOD) % MOD);
        tree[idx].lazy = (tree[idx].lazy + val) % MOD;
    }

    private void update(int idx, int l, int r, int ql, int qr, int val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            apply(idx, l, r, val);
            return;
        }
        if (tree[idx].lazy != 0 && l != r) {
            int mid = (l + r) / 2;
            apply(idx * 2, l, mid, tree[idx].lazy);
            apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy);
            tree[idx].lazy = 0;
        }
        int mid = (l + r) / 2;
        update(idx * 2, l, mid, ql, qr, val);
        update(idx * 2 + 1, mid + 1, r, ql, qr, val);
        tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD;
        tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % MOD;
    }
}
