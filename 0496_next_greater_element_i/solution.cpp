// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

#include <stack>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> nextGreaterElement(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> nextGreater;
        std::stack<int> monoStack;
        for (int num : nums2) {
            while (!monoStack.empty() && monoStack.top() < num) {
                nextGreater[monoStack.top()] = num;
                monoStack.pop();
            }
            monoStack.push(num);
        }
        std::vector<int> result;
        result.reserve(nums1.size());
        for (int num : nums1) {
            auto it = nextGreater.find(num);
            result.push_back(it == nextGreater.end() ? -1 : it->second);
        }
        return result;
    }
};
