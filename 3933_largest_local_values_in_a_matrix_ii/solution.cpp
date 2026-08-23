// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countLocalMaximums(std::vector<std::vector<int>>& matrix) {
        int rows = (int)matrix.size(), cols = (int)matrix[0].size();
        std::vector<std::vector<std::pair<int, int>>> positions(201);
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int value = matrix[row][col];
                if (value > 0) positions[value].push_back({row, col});
            }
        }
        int answer = 0;
        for (int value = 1; value <= 200; value++) {
            if (positions[value].empty()) continue;
            std::vector<std::vector<int>> prefix(rows + 1, std::vector<int>(cols + 1, 0));
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int add = matrix[row][col] > value ? 1 : 0;
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
                }
            }
            for (auto& [row, col] : positions[value]) {
                int top = std::max(0, row - value), bottom = std::min(rows - 1, row + value);
                int left = std::max(0, col - value), right = std::min(cols - 1, col + value);
                int greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
                for (int dr : {-value, value}) {
                    for (int dc : {-value, value}) {
                        int rr = row + dr, cc = col + dc;
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--;
                    }
                }
                if (greater == 0) answer++;
            }
        }
        return answer;
    }
};
