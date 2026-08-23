// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

#include <functional>

// JavaScript problem; C++ stand-in (immediate invoke; no timer runtime).
class Solution {
public:
    std::function<void()> debounce(std::function<void()> fn, int /*t*/) {
        return [fn]() { fn(); };
    }
};
