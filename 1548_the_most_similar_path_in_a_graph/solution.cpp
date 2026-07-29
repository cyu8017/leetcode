// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

#include <climits>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> mostSimilar(int n, std::vector<std::vector<int>>& roads,
                                 std::vector<std::string>& names,
                                 std::vector<std::string>& targetPath) {
        std::vector<std::vector<int>> graph(n);
        for (const auto& road : roads) {
            graph[road[0]].push_back(road[1]);
            graph[road[1]].push_back(road[0]);
        }

        std::vector<std::pair<int, std::vector<int>>> dp(n);
        for (int node = 0; node < n; ++node) {
            dp[node] = {names[node] != targetPath[0], {node}};
        }

        for (int i = 1; i < static_cast<int>(targetPath.size()); ++i) {
            std::vector<std::pair<int, std::vector<int>>> next_dp(n);
            for (int node = 0; node < n; ++node) {
                int best_cost = INT_MAX;
                std::vector<int> best_path;
                for (int previous : graph[node]) {
                    if (dp[previous].first < best_cost) {
                        best_cost = dp[previous].first;
                        best_path = dp[previous].second;
                    }
                }
                best_path.push_back(node);
                next_dp[node] = {best_cost + (names[node] != targetPath[i]), best_path};
            }
            dp = std::move(next_dp);
        }

        int best_cost = INT_MAX;
        std::vector<int> best_path;
        for (const auto& entry : dp) {
            if (entry.first < best_cost) {
                best_cost = entry.first;
                best_path = entry.second;
            }
        }
        return best_path;
    }
};
