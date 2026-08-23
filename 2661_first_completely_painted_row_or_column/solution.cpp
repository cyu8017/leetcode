// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

#include <vector>

class Solution {
public:
    int firstCompleteIndex(std::vector<int>& arr, std::vector<std::vector<int>>& mat) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        std::vector<std::pair<int,int>> pos(m * n + 1);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pos[mat[i][j]] = {i, j};
        std::vector<int> rowCnt(m), colCnt(n);
        for (int i = 0; i < (int)arr.size(); i++) {
            auto [r, c] = pos[arr[i]];
            rowCnt[r]++; colCnt[c]++;
            if (rowCnt[r] == n || colCnt[c] == m) return i;
        }
        return -1;
    }
};
