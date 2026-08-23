// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

#include <vector>

class Solution {
public:
    bool isBipartite(std::vector<std::vector<int>>& graph) {
        color_.assign(graph.size(), -1);
        for (int node = 0; node < static_cast<int>(graph.size()); ++node) {
            if (color_[node] == -1 && !dfs(graph, node, 0)) {
                return false;
            }
        }
        return true;
    }

private:
    std::vector<int> color_;

    bool dfs(std::vector<std::vector<int>>& graph, int node, int c) {
        color_[node] = c;
        for (int nei : graph[node]) {
            if (color_[nei] == -1) {
                if (!dfs(graph, nei, c ^ 1)) {
                    return false;
                }
            } else if (color_[nei] == c) {
                return false;
            }
        }
        return true;
    }
};
