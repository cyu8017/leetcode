// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

#include <algorithm>
#include <stack>
#include <vector>

class Solution {
public:
    int maximalRectangle(std::vector<std::vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }

        int cols = static_cast<int>(matrix[0].size());
        std::vector<int> heights(cols, 0);
        int maxArea = 0;

        for (const auto& row : matrix) {
            for (int j = 0; j < cols; ++j) {
                heights[j] = row[j] == '1' ? heights[j] + 1 : 0;
            }
            maxArea = std::max(maxArea, largestHistogram(heights));
        }

        return maxArea;
    }

private:
    int largestHistogram(std::vector<int> heights) {
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

        return maxArea;
    }
};
