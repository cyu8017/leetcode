// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumOperationsToWriteY(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        int cnt1[3] = {}, cnt2[3] = {};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int x = grid[i][j];
                bool a = i == j && i <= n / 2;
                bool b = i + j == n - 1 && i <= n / 2;
                bool c = j == n / 2 && i >= n / 2;
                if (a || b || c) cnt1[x]++;
                else cnt2[x]++;
            }
        }
        int ans = n * n;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (i != j) ans = std::min(ans, n * n - cnt1[i] - cnt2[j]);
        return ans;
    }
};
