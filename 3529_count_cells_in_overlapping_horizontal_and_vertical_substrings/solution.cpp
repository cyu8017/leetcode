// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

#include <string>
#include <vector>

class Solution {
public:
    int countCells(std::vector<std::vector<char>>& grid, std::string pattern) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::string row, col;
        row.reserve(m * n); col.reserve(m * n);
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) row.push_back(grid[i][j]);
        for (int j = 0; j < n; j++) for (int i = 0; i < m; i++) col.push_back(grid[i][j]);
        std::vector<std::vector<char>> hMark(m, std::vector<char>(n)), vMark(m, std::vector<char>(n));
        int plen = (int)pattern.size();
        for (int i = 0; i + plen <= (int)row.size(); i++) {
            if (row.compare(i, plen, pattern) == 0) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    hMark[pos / n][pos % n] = 1;
                }
            }
        }
        for (int i = 0; i + plen <= (int)col.size(); i++) {
            if (col.compare(i, plen, pattern) == 0) {
                for (int t = 0; t < plen; t++) {
                    int pos = i + t;
                    vMark[pos % m][pos / m] = 1;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)
            if (hMark[i][j] && vMark[i][j]) ans++;
        return ans;
    }
};
