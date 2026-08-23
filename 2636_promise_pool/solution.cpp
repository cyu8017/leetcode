// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

#include <functional>
#include <vector>

// JavaScript problem; C++ stand-in (sequential execution).
class Solution {
public:
    std::vector<int> promisePool(std::vector<std::function<int()>>& functions, int /*n*/) {
        std::vector<int> ans(functions.size());
        for (size_t i = 0; i < functions.size(); ++i) ans[i] = functions[i]();
        return ans;
    }
};
