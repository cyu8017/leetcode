// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int minCostToSupplyWater(int n, std::vector<int>& wells, std::vector<std::vector<int>>& pipes) {
        std::vector<int> parent(n + 1);
        std::iota(parent.begin(), parent.end(), 0);
        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        std::vector<std::vector<int>> edges = pipes;
        for (int i = 0; i < n; ++i) edges.push_back({0, i + 1, wells[i]});
        std::sort(edges.begin(), edges.end(), [](const auto& a, const auto& b) { return a[2] < b[2]; });
        int ans = 0;
        for (const auto& e : edges) {
            int ra = find(e[0]), rb = find(e[1]);
            if (ra == rb) continue;
            parent[rb] = ra;
            ans += e[2];
        }
        return ans;
    }
};
