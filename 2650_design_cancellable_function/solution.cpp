// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

#include <functional>
#include <utility>

class Solution {
public:
    // JS cancellable generator stand-in
    std::pair<std::function<void()>, std::function<std::pair<int,bool>()>> cancellable(std::function<int()> generator) {
        bool cancelled = false;
        bool done = false;
        int result = 0;
        auto cancel = [&cancelled]() { cancelled = true; };
        auto run = [&, generator]() -> std::pair<int,bool> {
            if (done) return {result, true};
            result = generator();
            done = true;
            return {result, !cancelled};
        };
        return {cancel, run};
    }
};
