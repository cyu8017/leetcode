// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

#include <vector>

class Solution {
    int find(std::vector<int>& parent, int node) {
        while (parent[node] != node) {
            parent[node] = parent[parent[node]];
            node = parent[node];
        }
        return node;
    }

    void unite(std::vector<int>& parent, int left, int right) {
        const int rootLeft = find(parent, left);
        const int rootRight = find(parent, right);
        if (rootLeft != rootRight) {
            parent[rootRight] = rootLeft;
        }
    }

public:
    int findCircleNum(std::vector<std::vector<int>>& isConnected) {
        const int n = static_cast<int>(isConnected.size());
        std::vector<int> parent(n);
        for (int index = 0; index < n; ++index) {
            parent[index] = index;
        }

        for (int row = 0; row < n; ++row) {
            for (int col = row + 1; col < n; ++col) {
                if (isConnected[row][col]) {
                    unite(parent, row, col);
                }
            }
        }

        int provinces = 0;
        for (int index = 0; index < n; ++index) {
            if (find(parent, index) == index) {
                provinces += 1;
            }
        }
        return provinces;
    }
};
