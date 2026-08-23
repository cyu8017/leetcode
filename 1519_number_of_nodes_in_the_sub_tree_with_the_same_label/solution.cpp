// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> countSubTrees(int n, std::vector<std::vector<int>>& edges, std::string labels) {
        std::vector<std::vector<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        std::vector<int> answer(n, 0);
        dfs(0, -1, graph, labels, answer);
        return answer;
    }

private:
    std::vector<int> dfs(int node, int parent, const std::vector<std::vector<int>>& graph,
                         const std::string& labels, std::vector<int>& answer) {
        std::vector<int> counts(26, 0);
        const int index = labels[node] - 'a';
        counts[index] = 1;
        for (int neighbor : graph[node]) {
            if (neighbor == parent) {
                continue;
            }
            const std::vector<int> child = dfs(neighbor, node, graph, labels, answer);
            for (int i = 0; i < 26; ++i) {
                counts[i] += child[i];
            }
        }
        answer[node] = counts[index];
        return counts;
    }
};
