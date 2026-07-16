// LeetCode 0378 - Kth Smallest Element in a Sorted Matrix
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

#include <vector>

class Solution {
public:
    int kthSmallest(std::vector<std::vector<int>>& matrix, int k) {
        int rows = static_cast<int>(matrix.size());
        int left = matrix[0][0];
        int right = matrix[rows - 1][rows - 1];

        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            int column = rows - 1;

            for (int row = 0; row < rows; ++row) {
                while (column >= 0 && matrix[row][column] > mid) {
                    --column;
                }
                count += column + 1;
            }

            if (count < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
};
