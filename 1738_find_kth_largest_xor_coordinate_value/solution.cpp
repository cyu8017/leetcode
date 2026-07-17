// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

#include <algorithm>
#include <vector>

class Solution {
public:
    int kthLargestValue(std::vector<std::vector<int>>& matrix, int k) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        std::vector<std::vector<int>> pref(rows + 1, std::vector<int>(cols + 1, 0));
        std::vector<int> values;
        values.reserve(rows * cols);
        for (int r = 1; r <= rows; r++) {
            for (int c = 1; c <= cols; c++) {
                pref[r][c] = pref[r - 1][c] ^ pref[r][c - 1] ^ pref[r - 1][c - 1] ^ matrix[r - 1][c - 1];
                values.push_back(pref[r][c]);
            }
        }
        std::nth_element(values.begin(), values.begin() + k - 1, values.end(), std::greater<int>());
        return values[k - 1];
    }
};
