// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countSquares(std::vector<std::vector<int>>& matrix) {
        int answer = 0;
        for (int r = 0; r < static_cast<int>(matrix.size()); ++r) {
            for (int c = 0; c < static_cast<int>(matrix[0].size()); ++c) {
                if (matrix[r][c] && r && c) {
                    matrix[r][c] += std::min({matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]});
                }
                answer += matrix[r][c];
            }
        }
        return answer;
    }
};
