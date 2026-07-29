// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

#include <string>
#include <vector>

class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int n = (int)strs.size(), m = (int)strs[0].size(), deleted = 0;
        std::vector<char> sortedPair(n - 1, 0);
        for (int c = 0; c < m; c++) {
            bool bad = false;
            for (int r = 0; r + 1 < n; r++) {
                if (!sortedPair[r] && strs[r][c] > strs[r + 1][c]) { bad = true; break; }
            }
            if (bad) { deleted++; continue; }
            for (int r = 0; r + 1 < n; r++)
                if (strs[r][c] < strs[r + 1][c]) sortedPair[r] = 1;
        }
        return deleted;
    }
};
