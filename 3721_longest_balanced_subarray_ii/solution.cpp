// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    struct Node {
        int l = 0, r = 0, mn = 0, mx = 0, lazy = 0;
    };

    struct SegmentTree {
        std::vector<Node> tr;

        explicit SegmentTree(int n) : tr(n << 2) { build(1, 0, n); }

        void build(int u, int l, int r) {
            tr[u] = {l, r, 0, 0, 0};
            if (l == r) return;
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }

        void apply(int u, int v) {
            tr[u].mn += v;
            tr[u].mx += v;
            tr[u].lazy += v;
        }

        void pushup(int u) {
            tr[u].mn = std::min(tr[u << 1].mn, tr[u << 1 | 1].mn);
            tr[u].mx = std::max(tr[u << 1].mx, tr[u << 1 | 1].mx);
        }

        void pushdown(int u) {
            if (tr[u].lazy != 0) {
                int v = tr[u].lazy;
                apply(u << 1, v);
                apply(u << 1 | 1, v);
                tr[u].lazy = 0;
            }
        }

        void modify(int u, int l, int r, int v) {
            if (tr[u].l >= l && tr[u].r <= r) {
                apply(u, v);
                return;
            }
            pushdown(u);
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (l <= mid) modify(u << 1, l, r, v);
            if (r > mid) modify(u << 1 | 1, l, r, v);
            pushup(u);
        }

        int query(int u, int target) {
            if (tr[u].l == tr[u].r) return tr[u].l;
            pushdown(u);
            int left = u << 1, right = u << 1 | 1;
            if (tr[left].mn <= target && target <= tr[left].mx) return query(left, target);
            return query(right, target);
        }
    };

public:
    int longestBalanced(std::vector<int>& nums) {
        int n = (int)nums.size();
        SegmentTree st(n);
        std::unordered_map<int, int> last;
        int now = 0, ans = 0;
        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int det = (x & 1) ? 1 : -1;
            auto it = last.find(x);
            if (it != last.end()) {
                st.modify(1, it->second, n, -det);
                now -= det;
            }
            last[x] = i;
            st.modify(1, i, n, det);
            now += det;
            int pos = st.query(1, now);
            ans = std::max(ans, i - pos);
        }
        return ans;
    }
};
