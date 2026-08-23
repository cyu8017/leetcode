// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

#include <vector>
#include <algorithm>

class Solution {
public:
    int totalSteps(std::vector<int>& nums) {
        std::vector<std::pair<int, int>> stack;
        int ans = 0;
        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            int steps = 0;
            while (!stack.empty() && nums[i] > stack.back().first) {
                steps = std::max(steps, stack.back().second);
                stack.pop_back();
                steps++;
            }
            ans = std::max(ans, steps);
            stack.push_back({nums[i], steps});
        }
        return ans;
    }
};
