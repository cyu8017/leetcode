// LeetCode 0042 - Trapping Rain Water
// https://leetcode.com/problems/trapping-rain-water/

#include <vector>

class Solution {
public:
    int trap(std::vector<int>& height) {
        if (height.empty()) {
            return 0;
        }

        int left = 0;
        int right = static_cast<int>(height.size()) - 1;
        int leftMax = 0;
        int rightMax = 0;
        int water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    water += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    water += rightMax - height[right];
                }
                right--;
            }
        }

        return water;
    }
};
