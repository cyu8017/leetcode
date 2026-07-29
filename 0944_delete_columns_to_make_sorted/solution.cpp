// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

#include <string>
#include <vector>

class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int ans = 0, m = (int)strs[0].size(), n = (int)strs.size();
        for (int c = 0; c < m; c++) {
            for (int r = 0; r + 1 < n; r++) {
                if (strs[r][c] > strs[r + 1][c]) { ans++; break; }
            }
        }
        return ans;
    }
};
