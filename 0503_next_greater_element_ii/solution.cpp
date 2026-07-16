// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

#include <stack>
#include <vector>

class Solution {
public:
    std::vector<int> nextGreaterElements(std::vector<int>& nums) {
        const int length = static_cast<int>(nums.size());
        std::vector<int> result(length, -1);
        std::stack<int> monoStack;
        for (int index = 0; index < length * 2; ++index) {
            const int value = nums[index % length];
            while (!monoStack.empty() && nums[monoStack.top()] < value) {
                result[monoStack.top()] = value;
                monoStack.pop();
            }
            if (index < length) {
                monoStack.push(index);
            }
        }
        return result;
    }
};
