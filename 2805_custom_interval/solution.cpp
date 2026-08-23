// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/
// JS-only problem; C++ stand-in returning a cancel flag setter.

#include <functional>

class Solution {
public:
    std::function<void()> customInterval(std::function<void()> fn, int delay, int period) {
        (void)fn; (void)delay; (void)period;
        bool cancelled = false;
        return [cancelled]() mutable { cancelled = true; };
    }
};
