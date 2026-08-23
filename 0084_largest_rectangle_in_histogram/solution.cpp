// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

#include <algorithm>
#include <stack>
#include <vector>

class Solution {
public:
    int largestRectangleArea(std::vector<int>& heights) {
        std::stack<int> stack;
        int maxArea = 0;
        heights.push_back(0);

        for (int i = 0; i < static_cast<int>(heights.size()); ++i) {
            int height = heights[i];
            while (!stack.empty() && heights[stack.top()] > height) {
                int h = heights[stack.top()];
                stack.pop();
                int width = stack.empty() ? i : i - stack.top() - 1;
                maxArea = std::max(maxArea, h * width);
            }
            stack.push(i);
        }

        heights.pop_back();
        return maxArea;
    }
};
