// LeetCode 1901 - Find a Peak Element II
// https://leetcode.com/problems/find-a-peak-element-ii/

#include <vector>

class Solution {
public:
    std::vector<int> findPeakGrid(std::vector<std::vector<int>>& mat) {
        int rows = (int)mat.size(), cols = (int)mat[0].size();
        int lo = 0, hi = cols - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int maxRow = 0;
            for (int r = 1; r < rows; r++) {
                if (mat[r][mid] > mat[maxRow][mid]) maxRow = r;
            }
            int left = mid ? mat[maxRow][mid - 1] : -1;
            int right = mid + 1 < cols ? mat[maxRow][mid + 1] : -1;
            if (mat[maxRow][mid] >= left && mat[maxRow][mid] >= right) {
                return {maxRow, mid};
            }
            if (left > mat[maxRow][mid]) hi = mid - 1;
            else lo = mid + 1;
        }
        return {0, 0};
    }
};
