// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

using System.Collections.Generic;

public class Solution {
    class Node {
        public int sum, sumSq, lazy;
    }

    public int SumCounts(int[] nums) {
        const int mod = 1000000007;
        int n = nums.Length;
        var last = new Dictionary<int, int>();
        var tree = new Node[4 * (n + 2)];
        for (int i = 0; i < tree.Length; i++) tree[i] = new Node();

        void Apply(int idx, int l, int r, int val) {
            int length = r - l + 1;
            tree[idx].sumSq = (int)((tree[idx].sumSq + 2L * val % mod * tree[idx].sum % mod +
                                     1L * val % mod * val % mod * length % mod) % mod);
            tree[idx].sum = (int)((tree[idx].sum + 1L * val % mod * length % mod) % mod);
            tree[idx].lazy = (tree[idx].lazy + val) % mod;
        }

        void Update(int idx, int l, int r, int ql, int qr, int val) {
            if (ql > r || qr < l) return;
            if (ql <= l && r <= qr) {
                Apply(idx, l, r, val);
                return;
            }
            if (tree[idx].lazy != 0 && l != r) {
                int mid = (l + r) / 2;
                Apply(idx * 2, l, mid, tree[idx].lazy);
                Apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy);
                tree[idx].lazy = 0;
            }
            int mid2 = (l + r) / 2;
            Update(idx * 2, l, mid2, ql, qr, val);
            Update(idx * 2 + 1, mid2 + 1, r, ql, qr, val);
            tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % mod;
            tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % mod;
        }

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            int prev = last.ContainsKey(v) ? last[v] : 0;
            Update(1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sumSq) % mod;
            last[v] = i;
        }
        return ans;
    }
}
