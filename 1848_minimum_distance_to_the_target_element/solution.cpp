// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    int getMinDistance(std::vector<int>& nums, int target, int start) {
        int best = static_cast<int>(nums.size());
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            if (nums[i] == target) {
                best = std::min(best, std::abs(i - start));
            }
        }
        return best;
    }
};
