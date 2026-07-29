// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int minimumCost(int n, std::vector<std::vector<int>>& connections) {
        std::vector<int> parent(n + 1);
        std::iota(parent.begin(), parent.end(), 0);
        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return false;
            parent[rb] = ra;
            return true;
        };
        std::sort(connections.begin(), connections.end(),
                  [](const auto& a, const auto& b) { return a[2] < b[2]; });
        int cost = 0, edges = 0;
        for (const auto& e : connections) {
            if (unite(e[0], e[1])) {
                cost += e[2];
                if (++edges == n - 1) return cost;
            }
        }
        return -1;
    }
};
