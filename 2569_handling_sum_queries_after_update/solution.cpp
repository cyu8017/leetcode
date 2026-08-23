// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

#include <vector>

class Solution {
public:
    std::vector<long long> handleQuery(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<std::vector<int>>& queries) {
        int n = (int)nums1.size();
        std::vector<int> ones(4 * n);
        std::vector<char> lazy(4 * n, 0);
        auto build = [&](auto&& self, int idx, int l, int r) -> void {
            if (l == r) {
                ones[idx] = nums1[l];
                return;
            }
            int m = (l + r) / 2;
            self(self, idx * 2, l, m);
            self(self, idx * 2 + 1, m + 1, r);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        };
        auto apply = [&](int idx, int l, int r) {
            ones[idx] = (r - l + 1) - ones[idx];
            lazy[idx] = !lazy[idx];
        };
        auto push = [&](int idx, int l, int r) {
            if (lazy[idx] && l != r) {
                int m = (l + r) / 2;
                apply(idx * 2, l, m);
                apply(idx * 2 + 1, m + 1, r);
                lazy[idx] = 0;
            }
        };
        auto update = [&](auto&& self, int idx, int l, int r, int ql, int qr) -> void {
            if (ql <= l && r <= qr) {
                apply(idx, l, r);
                return;
            }
            push(idx, l, r);
            int m = (l + r) / 2;
            if (ql <= m) self(self, idx * 2, l, m, ql, qr);
            if (qr > m) self(self, idx * 2 + 1, m + 1, r, ql, qr);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        };
        build(build, 1, 0, n - 1);
        long long sum2 = 0;
        for (int x : nums2) sum2 += x;
        std::vector<long long> ans;
        for (auto& q : queries) {
            if (q[0] == 1) update(update, 1, 0, n - 1, q[1], q[2]);
            else if (q[0] == 2) sum2 += (long long)q[1] * ones[1];
            else ans.push_back(sum2);
        }
        return ans;
    }
};
