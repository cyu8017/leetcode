// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

#include <vector>

class Solution {
public:
    int findChampion(std::vector<std::vector<int>>& grid) {
        int n = (int)grid.size();
        for (int i = 0; i < n; i++) {
            bool win = true;
            for (int j = 0; j < n; j++)
                if (i != j && grid[i][j] == 0) { win = false; break; }
            if (win) return i;
        }
        return -1;
    }
};
