// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

#include <algorithm>
#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    int maximalNetworkRank(int n, std::vector<std::vector<int>>& roads) {
        std::vector<int> degree(n, 0);
        std::set<std::pair<int, int>> edges;
        for (const auto& road : roads) {
            int a = road[0], b = road[1];
            ++degree[a];
            ++degree[b];
            if (a > b) {
                std::swap(a, b);
            }
            edges.insert({a, b});
        }
        int ans = 0;
        for (int a = 0; a < n; ++a) {
            for (int b = a + 1; b < n; ++b) {
                ans = std::max(ans, degree[a] + degree[b] - (edges.count({a, b}) ? 1 : 0));
            }
        }
        return ans;
    }
};
