// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

#include <utility>
#include <vector>

class Solution {
public:
    int deleteTreeNodes(int nodes, std::vector<int>& parent, std::vector<int>& value) {
        std::vector<std::vector<int>> children(nodes);
        for (int node = 1; node < nodes; ++node) {
            children[parent[node]].push_back(node);
        }
        auto dfs = [&](auto&& self, int node) -> std::pair<int, int> {
            int total = value[node], count = 1;
            for (int child : children[node]) {
                auto [childSum, childCount] = self(self, child);
                total += childSum;
                count += childCount;
            }
            return {total, total == 0 ? 0 : count};
        };
        return dfs(dfs, 0).second;
    }
};
