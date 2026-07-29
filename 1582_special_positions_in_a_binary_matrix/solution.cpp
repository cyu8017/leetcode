// LeetCode 1582 - Special Positions in a Binary Matrix
// https://leetcode.com/problems/special-positions-in-a-binary-matrix/

#include <vector>

class Solution {
public:
    int numSpecial(std::vector<std::vector<int>>& mat) {
        const int m = static_cast<int>(mat.size());
        const int n = static_cast<int>(mat[0].size());
        std::vector<int> rows(m, 0);
        std::vector<int> cols(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rows[i] += mat[i][j];
                cols[j] += mat[i][j];
            }
        }
        int answer = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1 && rows[i] == 1 && cols[j] == 1) {
                    ++answer;
                }
            }
        }
        return answer;
    }
};
