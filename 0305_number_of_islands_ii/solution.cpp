// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

#include <unordered_map>
#include <vector>

class Solution {
    std::unordered_map<int, int> parent;
    std::unordered_map<int, int> rank;

    int find(int index) {
        if (parent.find(index) == parent.end()) {
            parent[index] = index;
            rank[index] = 0;
        }
        if (parent[index] != index) {
            parent[index] = find(parent[index]);
        }
        return parent[index];
    }

    bool unite(int left, int right) {
        int rootLeft = find(left);
        int rootRight = find(right);
        if (rootLeft == rootRight) {
            return false;
        }
        if (rank[rootLeft] < rank[rootRight]) {
            std::swap(rootLeft, rootRight);
        }
        parent[rootRight] = rootLeft;
        if (rank[rootLeft] == rank[rootRight]) {
            rank[rootLeft] += 1;
        }
        return true;
    }

public:
    std::vector<int> numIslands2(int m, int n, std::vector<std::vector<int>>& positions) {
        std::vector<int> result;
        int islands = 0;
        const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (const std::vector<int>& position : positions) {
            int row = position[0];
            int col = position[1];
            int index = row * n + col;
            if (parent.find(index) != parent.end()) {
                result.push_back(islands);
                continue;
            }
            parent[index] = index;
            rank[index] = 0;
            islands += 1;
            for (const auto& direction : directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n) {
                    int neighbor = nextRow * n + nextCol;
                    if (parent.find(neighbor) != parent.end() && unite(index, neighbor)) {
                        islands -= 1;
                    }
                }
            }
            result.push_back(islands);
        }

        return result;
    }
};
