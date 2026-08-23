// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

#include <vector>

class Solution {
public:
    int countServers(std::vector<std::vector<int>>& grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        std::vector<int> rows(m, 0), cols(n, 0);
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                rows[r] += grid[r][c];
                cols[c] += grid[r][c];
            }
        }
        int answer = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] && (rows[r] > 1 || cols[c] > 1)) {
                    ++answer;
                }
            }
        }
        return answer;
    }
};
