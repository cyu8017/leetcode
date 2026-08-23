// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums, int k) {
        int maxV = 0;
        for (int x : nums) maxV = std::max(maxV, x);
        SegTree st(maxV + 1);
        int ans = 0;
        for (int x : nums) {
            int lo = std::max(1, x - k);
            int best = 1;
            if (lo <= x - 1) best = st.query(1, 1, maxV, lo, x - 1) + 1;
            st.update(1, 1, maxV, x, best);
            ans = std::max(ans, best);
        }
        return ans;
    }

private:
    struct SegTree {
        int n;
        std::vector<int> tree;
        SegTree(int n) : n(n), tree(4 * n) {}
        void update(int idx, int l, int r, int pos, int val) {
            if (l == r) {
                tree[idx] = std::max(tree[idx], val);
                return;
            }
            int mid = (l + r) / 2;
            if (pos <= mid) update(idx * 2, l, mid, pos, val);
            else update(idx * 2 + 1, mid + 1, r, pos, val);
            tree[idx] = std::max(tree[idx * 2], tree[idx * 2 + 1]);
        }
        int query(int idx, int l, int r, int ql, int qr) {
            if (qr < l || r < ql) return 0;
            if (ql <= l && r <= qr) return tree[idx];
            int mid = (l + r) / 2;
            return std::max(query(idx * 2, l, mid, ql, qr), query(idx * 2 + 1, mid + 1, r, ql, qr));
        }
    };
};
