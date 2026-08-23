// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

#include <vector>

class Solution {
public:
    std::vector<int> stableMountains(std::vector<int>& height, int threshold) {
        std::vector<int> ans;
        for (int i = 1; i < (int)height.size(); i++) {
            if (height[i - 1] > threshold) ans.push_back(i);
        }
        return ans;
    }
};
