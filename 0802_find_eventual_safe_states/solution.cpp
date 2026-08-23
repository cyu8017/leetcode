// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> eventualSafeNodes(std::vector<std::vector<int>>& graph) {
        int n = static_cast<int>(graph.size());
        std::vector<int> color(n, 0);
        std::function<bool(int)> dfs = [&](int node) -> bool {
            if (color[node]) {
                return color[node] == 2;
            }
            color[node] = 1;
            for (int nei : graph[node]) {
                if (!dfs(nei)) {
                    return false;
                }
            }
            color[node] = 2;
            return true;
        };
        std::vector<int> ans;
        for (int i = 0; i < n; ++i) {
            if (dfs(i)) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
