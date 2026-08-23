// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

#include <vector>

class Solution {
public:
    int numberOfSubmatrices(std::vector<std::vector<char>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<std::vector<std::vector<int>>> s(m + 1, std::vector<std::vector<int>>(n + 1, std::vector<int>(2)));
        int ans = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0];
                if (grid[i - 1][j - 1] == 'X') s[i][j][0]++;
                s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1];
                if (grid[i - 1][j - 1] == 'Y') s[i][j][1]++;
                if (s[i][j][0] > 0 && s[i][j][0] == s[i][j][1]) ans++;
            }
        }
        return ans;
    }
};
