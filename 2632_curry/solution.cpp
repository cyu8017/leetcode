// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in applying all args at once.
class Solution {
public:
    std::function<int(const std::vector<int>&)> curry(std::function<int(const std::vector<int>&)> fn, int /*arity*/) {
        return [fn](const std::vector<int>& args) { return fn(args); };
    }
};
