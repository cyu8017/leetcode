// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

#include <algorithm>
#include <vector>

class Solution {
public:
    int largestSubmatrix(std::vector<std::vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        std::vector<int> heights(n, 0);
        int best = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                heights[c] = matrix[r][c] ? heights[c] + 1 : 0;
            }
            std::vector<int> sorted = heights;
            std::sort(sorted.begin(), sorted.end(), std::greater<int>());
            for (int width = 1; width <= n; width++) {
                best = std::max(best, width * sorted[width - 1]);
            }
        }
        return best;
    }
};
