// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

#include <map>
#include <vector>

class Solution {
public:
    int equalPairs(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        std::map<std::vector<int>, int> freq;
        for (int i = 0; i < n; i++) freq[grid[i]]++;
        int ans = 0;
        std::vector<int> col(n);
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) col[i] = grid[i][j];
            ans += freq[col];
        }
        return ans;
    }
};
