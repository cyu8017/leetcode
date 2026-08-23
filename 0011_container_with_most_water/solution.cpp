// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0;
        int right = static_cast<int>(height.size()) - 1;
        int best = 0;

        while (left < right) {
            int width = right - left;
            best = std::max(best, std::min(height[left], height[right]) * width);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return best;
    }
};
