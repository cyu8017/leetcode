// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

#include <algorithm>
#include <vector>

class Solution {
    int find(std::vector<int>& parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);
        }
        return parent[node];
    }

public:
    int countComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> parent(n);
        std::vector<int> rank(n, 0);
        for (int node = 0; node < n; node++) {
            parent[node] = node;
        }

        int components = n;
        for (const std::vector<int>& edge : edges) {
            int left = edge[0];
            int right = edge[1];
            int rootLeft = find(parent, left);
            int rootRight = find(parent, right);
            if (rootLeft == rootRight) {
                continue;
            }
            if (rank[rootLeft] < rank[rootRight]) {
                std::swap(rootLeft, rootRight);
            }
            parent[rootRight] = rootLeft;
            if (rank[rootLeft] == rank[rootRight]) {
                rank[rootLeft] += 1;
            }
            components -= 1;
        }
        return components;
    }
};
