// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findContentChildren(std::vector<int>& g, std::vector<int>& s) {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());

        int child = 0;
        for (int cookie : s) {
            if (child < static_cast<int>(g.size()) && cookie >= g[child]) {
                ++child;
            }
        }
        return child;
    }
};
