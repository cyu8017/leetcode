// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

#include <functional>
#include <optional>

class Solution {
public:
    // JS timeout cancellation stand-in
    std::pair<std::function<void()>, std::function<std::optional<int>()>> cancellable(
        std::function<int()> fn, int /*t*/) {
        bool cancelled = false;
        auto cancel = [&cancelled]() { cancelled = true; };
        auto result = [fn, &cancelled]() -> std::optional<int> {
            if (cancelled) return std::nullopt;
            return fn();
        };
        return {cancel, result};
    }
};
