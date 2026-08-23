// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int(int)> compose(std::vector<std::function<int(int)>> functions) {
        return [functions](int x) {
            for (int i = (int)functions.size() - 1; i >= 0; --i) x = functions[i](x);
            return x;
        };
    }
};
