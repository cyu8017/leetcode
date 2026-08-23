// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

#include <vector>
#include <unordered_set>

class Solution {
public:
    int maxWeight(int n, std::vector<std::vector<int>>& edges, int k, int t) {
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        for (auto& e : edges) graph[e[0]].push_back({e[1], e[2]});
        std::vector<std::vector<std::unordered_set<int>>> dp(n, std::vector<std::unordered_set<int>>(k + 1));
        for (int u = 0; u < n; u++) dp[u][0].insert(0);
        for (int i = 0; i < k; i++) {
            for (int u = 0; u < n; u++) {
                for (int sum : dp[u][i]) {
                    for (auto& [to, w] : graph[u]) {
                        int ns = sum + w;
                        if (ns < t) dp[to][i + 1].insert(ns);
                    }
                }
            }
        }
        int ans = -1;
        for (int u = 0; u < n; u++)
            for (int sum : dp[u][k]) if (sum > ans) ans = sum;
        return ans;
    }
};
