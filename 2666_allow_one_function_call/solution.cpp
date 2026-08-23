// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

#include <functional>
#include <optional>

class Solution {
public:
    // JS once stand-in
    std::function<std::optional<int>(int)> once(std::function<int(int)> fn) {
        bool called = false;
        int res = 0;
        return [fn, called, res](int arg) mutable -> std::optional<int> {
            if (called) return std::nullopt;
            called = true;
            res = fn(arg);
            return res;
        };
    }
};
