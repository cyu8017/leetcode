// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minFlips(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        int cnt1 = 0, cnt2 = 0;
        for (auto& row : grid) {
            for (int j = 0; j < n / 2; j++) {
                if (row[j] != row[n - j - 1]) cnt1++;
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m / 2; i++) {
                if (grid[i][j] != grid[m - i - 1][j]) cnt2++;
            }
        }
        return std::min(cnt1, cnt2);
    }
};
