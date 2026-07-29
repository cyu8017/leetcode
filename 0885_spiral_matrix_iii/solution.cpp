// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> spiralMatrixIII(int rows, int cols, int rStart,
                                                  int cStart) {
        std::vector<std::vector<int>> ans{{rStart, cStart}};
        if (rows * cols == 1) {
            return ans;
        }
        int r = rStart, c = cStart;
        const int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int steps = 1;
        while (static_cast<int>(ans.size()) < rows * cols) {
            for (int d = 0; d < 4; ++d) {
                int dr = dirs[d][0], dc = dirs[d][1];
                for (int i = 0; i < steps; ++i) {
                    r += dr;
                    c += dc;
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans.push_back({r, c});
                        if (static_cast<int>(ans.size()) == rows * cols) {
                            return ans;
                        }
                    }
                }
                if (d % 2 == 1) {
                    ++steps;
                }
            }
        }
        return ans;
    }
};
