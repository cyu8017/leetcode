// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

#include <algorithm>
#include <vector>

class Solution {
public:
    int deleteGreatestValue(std::vector<std::vector<int>>& grid) {
        for (auto& row : grid) std::sort(row.begin(), row.end());
        int ans = 0, n = (int)grid[0].size();
        for (int c = 0; c < n; c++) {
            int mx = 0;
            for (auto& row : grid) if (row[c] > mx) mx = row[c];
            ans += mx;
        }
        return ans;
    }
};
