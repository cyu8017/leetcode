// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> largeGroupPositions(std::string s) {
        std::vector<std::vector<int>> ans;
        int n = static_cast<int>(s.size());
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) {
                ++j;
            }
            if (j - i >= 3) {
                ans.push_back({i, j - 1});
            }
            i = j;
        }
        return ans;
    }
};
