// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

#include <vector>
#include <algorithm>

class Solution {
    struct Node {
        int l = 0, r = 0;
        int s00 = 0, s01 = 0, s10 = 0, s11 = 0;
    };
    std::vector<Node> tr;
    void build(int u, int l, int r) {
        tr[u].l = l; tr[u].r = r;
        if (l == r) return;
        int mid = (l + r) >> 1;
        build(u << 1, l, mid);
        build(u << 1 | 1, mid + 1, r);
    }
    void pushup(int u) {
        Node& left = tr[u << 1];
        Node& right = tr[u << 1 | 1];
        tr[u].s00 = std::max(left.s00 + right.s10, left.s01 + right.s00);
        tr[u].s01 = std::max(left.s00 + right.s11, left.s01 + right.s01);
        tr[u].s10 = std::max(left.s10 + right.s10, left.s11 + right.s00);
        tr[u].s11 = std::max(left.s10 + right.s11, left.s11 + right.s01);
    }
    void modify(int u, int x, int v) {
        if (tr[u].l == tr[u].r) {
            tr[u].s11 = std::max(0, v);
            return;
        }
        int mid = (tr[u].l + tr[u].r) >> 1;
        if (x <= mid) modify(u << 1, x, v);
        else modify(u << 1 | 1, x, v);
        pushup(u);
    }
    int query(int u, int l, int r) {
        if (tr[u].l >= l && tr[u].r <= r) return tr[u].s11;
        int mid = (tr[u].l + tr[u].r) >> 1;
        int ans = 0;
        if (r <= mid) ans = query(u << 1, l, r);
        if (l > mid) ans = std::max(ans, query(u << 1 | 1, l, r));
        return ans;
    }
public:
    int maximumSumSubsequence(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        tr.assign(n * 4, {});
        build(1, 1, n);
        for (int i = 0; i < n; i++) modify(1, i + 1, nums[i]);
        const int mod = 1e9 + 7;
        int ans = 0;
        for (auto& q : queries) {
            modify(1, q[0] + 1, q[1]);
            ans = (ans + query(1, 1, n)) % mod;
        }
        return ans;
    }
};
