// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

#include <climits>
#include <stack>
#include <vector>

class Solution {
public:
    bool find132pattern(std::vector<int>& nums) {
        std::stack<int> candidates;
        int third = INT_MIN;

        for (int index = static_cast<int>(nums.size()) - 1; index >= 0; --index) {
            if (nums[index] < third) {
                return true;
            }
            while (!candidates.empty() && nums[index] > candidates.top()) {
                third = candidates.top();
                candidates.pop();
            }
            candidates.push(nums[index]);
        }
        return false;
    }
};
