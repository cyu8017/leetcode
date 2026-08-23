// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/
// JS-only problem; C++ stand-in.

#include <functional>

class Solution {
public:
    std::function<int()> promisify(std::function<void()> fn) {
        (void)fn;
        return []() { return 0; };
    }
};
