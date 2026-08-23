// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> maximumSegmentSum(std::vector<int>& nums, std::vector<int>& removeQueries) {
        int n = (int)nums.size();
        std::vector<int> parent(n);
        std::vector<long long> sum(n);
        std::vector<char> active(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            if (parent[x] != x) parent[x] = self(self, parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(find, a), rb = find(find, b);
            if (ra == rb) return;
            parent[rb] = ra;
            sum[ra] += sum[rb];
        };
        std::vector<long long> ans(n);
        long long best = 0;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = best;
            int idx = removeQueries[i];
            active[idx] = 1;
            sum[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) unite(idx, idx - 1);
            if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1);
            best = std::max(best, sum[find(find, idx)]);
        }
        return ans;
    }
};
