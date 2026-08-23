// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

#include <functional>
#include <chrono>

class Solution {
public:
    // JS throttle stand-in: calls fn at most once per t ms (wall clock)
    std::function<void()> throttle(std::function<void()> fn, int t) {
        auto last = std::chrono::steady_clock::now() - std::chrono::hours(24);
        return [fn, t, last]() mutable {
            auto now = std::chrono::steady_clock::now();
            if (std::chrono::duration_cast<std::chrono::milliseconds>(now - last).count() >= t) {
                last = now;
                fn();
            }
        };
    }
};
