// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

#include <algorithm>
#include <array>
#include <numeric>
#include <vector>

class Solution {
    std::vector<int> parent_;

    int find(int x) {
        while (x != parent_[x]) {
            parent_[x] = parent_[parent_[x]];
            x = parent_[x];
        }
        return x;
    }

public:
    std::vector<bool> distanceLimitedPathsExist(
        int n, std::vector<std::vector<int>>& edgeList, std::vector<std::vector<int>>& queries) {
        parent_.resize(n);
        std::iota(parent_.begin(), parent_.end(), 0);
        std::vector<bool> ans(queries.size(), false);
        std::sort(edgeList.begin(), edgeList.end(), [](const auto& a, const auto& b) {
            return a[2] < b[2];
        });
        std::vector<std::array<int, 4>> qs;
        qs.reserve(queries.size());
        for (int j = 0; j < static_cast<int>(queries.size()); ++j) {
            qs.push_back({queries[j][2], queries[j][0], queries[j][1], j});
        }
        std::sort(qs.begin(), qs.end());
        int i = 0;
        for (const auto& q : qs) {
            int limit = q[0];
            int p = q[1];
            int r = q[2];
            int idx = q[3];
            while (i < static_cast<int>(edgeList.size()) && edgeList[i][2] < limit) {
                int a = find(edgeList[i][0]);
                int b = find(edgeList[i][1]);
                parent_[a] = b;
                ++i;
            }
            ans[idx] = find(p) == find(r);
        }
        return ans;
    }
};
