// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

#include <functional>
#include <stdexcept>

// JavaScript problem; C++ stand-in (no real timeout).
class Solution {
public:
    std::function<int()> timeLimit(std::function<int()> fn, int /*t*/) {
        return [fn]() { return fn(); };
    }
};
