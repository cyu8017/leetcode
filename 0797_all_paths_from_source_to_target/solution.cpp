// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> allPathsSourceTarget(std::vector<std::vector<int>>& graph) {
        target_ = static_cast<int>(graph.size()) - 1;
        answer_.clear();
        std::vector<int> path{0};
        dfs(graph, 0, path);
        return answer_;
    }

private:
    int target_;
    std::vector<std::vector<int>> answer_;

    void dfs(std::vector<std::vector<int>>& graph, int node, std::vector<int>& path) {
        if (node == target_) {
            answer_.push_back(path);
            return;
        }
        for (int nei : graph[node]) {
            path.push_back(nei);
            dfs(graph, nei, path);
            path.pop_back();
        }
    }
};
