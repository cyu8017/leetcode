// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

#include <algorithm>
#include <vector>

class Solution {
public:
    int largest1BorderedSquare(std::vector<std::vector<int>>& grid) {
        int m = static_cast<int>(grid.size()), n = static_cast<int>(grid[0].size());
        std::vector<std::vector<int>> left(m, std::vector<int>(n)), up(m, std::vector<int>(n));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c]) {
                    left[r][c] = 1 + (c ? left[r][c - 1] : 0);
                    up[r][c] = 1 + (r ? up[r - 1][c] : 0);
                }
            }
        }
        int best = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (!grid[r][c]) continue;
                int limit = std::min(left[r][c], up[r][c]);
                for (int size = limit; size > 0; --size) {
                    if (left[r - size + 1][c] >= size && up[r][c - size + 1] >= size) {
                        best = std::max(best, size);
                        break;
                    }
                }
            }
        }
        return best * best;
    }
};
