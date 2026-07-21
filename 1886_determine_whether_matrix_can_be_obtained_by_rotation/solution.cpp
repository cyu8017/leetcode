// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

#include <vector>

class Solution {
public:
    bool findRotation(std::vector<std::vector<int>>& mat, std::vector<std::vector<int>>& target) {
        std::vector<std::vector<int>> current = mat;
        for (int r = 0; r < 4; r++) {
            if (current == target) {
                return true;
            }
            int n = static_cast<int>(current.size());
            std::vector<std::vector<int>> rotated(n, std::vector<int>(n));
            for (int col = 0; col < n; col++) {
                for (int row = 0; row < n; row++) {
                    rotated[col][row] = current[n - 1 - row][col];
                }
            }
            current.swap(rotated);
        }
        return false;
    }
};
