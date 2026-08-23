// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

#include <vector>

class Solution {
public:
    int oddCells(int m, int n, std::vector<std::vector<int>>& indices) {
        std::vector<int> rows(m, 0), cols(n, 0);
        for (const auto& idx : indices) {
            rows[idx[0]] ^= 1;
            cols[idx[1]] ^= 1;
        }
        int answer = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                answer += rows[r] ^ cols[c];
            }
        }
        return answer;
    }
};
