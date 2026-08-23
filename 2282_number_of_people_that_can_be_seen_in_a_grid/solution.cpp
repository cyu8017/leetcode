// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> seePeople(std::vector<std::vector<int>>& heights) {
        int m = (int)heights.size(), n = (int)heights[0].size();
        std::vector<std::vector<int>> ans(m, std::vector<int>(n));
        for (int i = 0; i < m; ++i) {
            std::vector<int> stack;
            for (int j = n - 1; j >= 0; --j) {
                int cnt = 0;
                while (!stack.empty() && heights[i][stack.back()] < heights[i][j]) { stack.pop_back(); cnt++; }
                if (!stack.empty()) cnt++;
                ans[i][j] += cnt;
                while (!stack.empty() && heights[i][stack.back()] == heights[i][j]) stack.pop_back();
                stack.push_back(j);
            }
        }
        for (int j = 0; j < n; ++j) {
            std::vector<int> stack;
            for (int i = m - 1; i >= 0; --i) {
                int cnt = 0;
                while (!stack.empty() && heights[stack.back()][j] < heights[i][j]) { stack.pop_back(); cnt++; }
                if (!stack.empty()) cnt++;
                ans[i][j] += cnt;
                while (!stack.empty() && heights[stack.back()][j] == heights[i][j]) stack.pop_back();
                stack.push_back(i);
            }
        }
        return ans;
    }
};
