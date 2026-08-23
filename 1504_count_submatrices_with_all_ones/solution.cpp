// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

#include <utility>
#include <vector>

class Solution {
public:
    int numSubmat(std::vector<std::vector<int>>& mat) {
        int ans = 0;
        const int cols = static_cast<int>(mat[0].size());
        std::vector<int> heights(cols, 0);
        for (const auto& row : mat) {
            for (int j = 0; j < cols; ++j) {
                heights[j] = row[j] ? heights[j] + 1 : 0;
            }
            std::vector<std::pair<int, int>> stack;
            int running = 0;
            for (int h : heights) {
                int count = 1;
                while (!stack.empty() && stack.back().first >= h) {
                    running -= stack.back().first * stack.back().second;
                    count += stack.back().second;
                    stack.pop_back();
                }
                stack.emplace_back(h, count);
                running += h * count;
                ans += running;
            }
        }
        return ans;
    }
};
