// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

#include <numeric>
#include <vector>

class Solution {
    struct Node {
        int l = 0, r = 0, g = 0;
    };

    struct SegmentTree {
        std::vector<Node> tr;
        explicit SegmentTree(int n) : tr(n << 2) { build(1, 1, n); }

        void build(int u, int l, int r) {
            tr[u] = {l, r, 0};
            if (l == r) return;
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }

        void pushup(int u) { tr[u].g = std::gcd(tr[u << 1].g, tr[u << 1 | 1].g); }

        void modify(int u, int x, int v) {
            if (tr[u].l == tr[u].r) {
                tr[u].g = v;
                return;
            }
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (x <= mid) modify(u << 1, x, v);
            else modify(u << 1 | 1, x, v);
            pushup(u);
        }

        int query(int u, int l, int r) {
            if (l > r) return 0;
            if (tr[u].l >= l && tr[u].r <= r) return tr[u].g;
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (r <= mid) return query(u << 1, l, r);
            if (l > mid) return query(u << 1 | 1, l, r);
            return std::gcd(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r));
        }
    };

public:
    int countGoodSubseq(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        SegmentTree tree(n);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % p == 0) {
                tree.modify(1, i + 1, nums[i]);
                cnt++;
            }
        }
        int ans = 0;
        for (auto& q : queries) {
            int idx = q[0], val = q[1];
            if (nums[idx] % p == 0) {
                tree.modify(1, idx + 1, 0);
                cnt--;
            }
            if (val % p == 0) {
                tree.modify(1, idx + 1, val);
                cnt++;
            }
            nums[idx] = val;
            if (tree.tr[1].g != p) continue;
            if (cnt < n || n > 6) {
                ans++;
                continue;
            }
            for (int i = 1; i <= n; i++) {
                int leftG = tree.query(1, 1, i - 1);
                int rightG = tree.query(1, i + 1, n);
                if (std::gcd(leftG, rightG) == p) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
};
