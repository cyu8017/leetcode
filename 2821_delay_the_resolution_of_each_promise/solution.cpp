// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/
// JS-only problem; C++ stand-in wrapping callables.

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<std::function<int()>> delayAll(std::vector<std::function<int()>>& functions, int ms) {
        (void)ms;
        std::vector<std::function<int()>> out;
        for (auto& f : functions) out.push_back(f);
        return out;
    }
};
