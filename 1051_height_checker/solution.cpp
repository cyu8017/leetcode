// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

#include <algorithm>
#include <vector>

class Solution {
public:
    int heightChecker(std::vector<int>& heights) {
        std::vector<int> sorted = heights;
        std::sort(sorted.begin(), sorted.end());
        int ans = 0;
        for (size_t i = 0; i < heights.size(); ++i) {
            if (heights[i] != sorted[i]) {
                ++ans;
            }
        }
        return ans;
    }
};
