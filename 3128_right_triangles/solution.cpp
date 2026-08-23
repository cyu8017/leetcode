// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

#include <vector>

class Solution {
public:
    long long numberOfRightTriangles(std::vector<std::vector<int>>& grid) {
        int m = (int)grid.size(), n = (int)grid[0].size();
        std::vector<int> rows(m), cols(n);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                rows[i] += grid[i][j];
                cols[j] += grid[i][j];
            }
        long long ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1)
                    ans += 1LL * (rows[i] - 1) * (cols[j] - 1);
        return ans;
    }
};
