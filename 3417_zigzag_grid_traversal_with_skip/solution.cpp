// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

#include <vector>

class Solution {
public:
    std::vector<int> zigzagTraversal(std::vector<std::vector<int>>& grid) {
        std::vector<int> ans;
        bool skip = false;
        for (int i = 0; i < (int)grid.size(); i++) {
            auto& row = grid[i];
            if (i % 2 == 0) {
                for (int v : row) {
                    if (!skip) ans.push_back(v);
                    skip = !skip;
                }
            } else {
                for (int j = (int)row.size() - 1; j >= 0; j--) {
                    if (!skip) ans.push_back(row[j]);
                    skip = !skip;
                }
            }
        }
        return ans;
    }
};
