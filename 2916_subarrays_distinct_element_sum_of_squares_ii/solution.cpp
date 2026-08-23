// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int sumCounts(std::vector<int>& nums) {
        const int mod = 1000000007;
        int n = (int)nums.size();
        std::unordered_map<int, int> last;
        struct Node { int sum = 0, sumSq = 0, lazy = 0; };
        std::vector<Node> tree(4 * (n + 2));
        auto apply = [&](int idx, int l, int r, int val) {
            int length = r - l + 1;
            tree[idx].sumSq = (int)((tree[idx].sumSq + 2LL * val % mod * tree[idx].sum % mod +
                                     1LL * val % mod * val % mod * length % mod) % mod);
            tree[idx].sum = (int)((tree[idx].sum + 1LL * val % mod * length % mod) % mod);
            tree[idx].lazy = (tree[idx].lazy + val) % mod;
        };
        std::function<void(int, int, int, int, int, int)> update = [&](int idx, int l, int r, int ql, int qr, int val) {
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
            tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % mod;
            tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % mod;
        };
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1];
            int prev = last.count(v) ? last[v] : 0;
            update(1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sumSq) % mod;
            last[v] = i;
        }
        return ans;
    }
};
