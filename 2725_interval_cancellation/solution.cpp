// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

#include <functional>
#include <vector>

class Solution {
public:
    // JS interval cancellation stand-in
    std::pair<std::function<void()>, std::vector<int>> cancellable(
        std::function<int()> fn, int /*t*/, int times) {
        bool cancelled = false;
        std::vector<int> results;
        for (int i = 0; i < times && !cancelled; i++) results.push_back(fn());
        auto cancel = [&cancelled]() { cancelled = true; };
        return {cancel, results};
    }
};
