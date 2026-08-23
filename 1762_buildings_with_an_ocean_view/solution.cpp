// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> findBuildings(std::vector<int>& heights) {
        std::vector<int> ans;
        int tallest = 0;
        for (int i = (int)heights.size() - 1; i >= 0; i--) {
            if (heights[i] > tallest) {
                ans.push_back(i);
                tallest = heights[i];
            }
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
