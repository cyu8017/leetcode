// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

#include <vector>

class Solution {
public:
    std::vector<int> findMinHeightTrees(int n, std::vector<std::vector<int>>& edges) {
        if (n <= 2) {
            std::vector<int> nodes;
            for (int node = 0; node < n; node++) {
                nodes.push_back(node);
            }
            return nodes;
        }

        std::vector<std::vector<int>> graph(n);
        std::vector<int> degree(n, 0);
        for (const std::vector<int>& edge : edges) {
            int left = edge[0];
            int right = edge[1];
            graph[left].push_back(right);
            graph[right].push_back(left);
            degree[left] += 1;
            degree[right] += 1;
        }

        std::vector<int> leaves;
        for (int node = 0; node < n; node++) {
            if (degree[node] == 1) {
                leaves.push_back(node);
            }
        }

        int remaining = n;
        while (remaining > 2) {
            remaining -= static_cast<int>(leaves.size());
            std::vector<int> newLeaves;
            for (int leaf : leaves) {
                for (int neighbor : graph[leaf]) {
                    degree[neighbor] -= 1;
                    if (degree[neighbor] == 1) {
                        newLeaves.push_back(neighbor);
                    }
                }
            }
            leaves = newLeaves;
        }

        return leaves;
    }
};
