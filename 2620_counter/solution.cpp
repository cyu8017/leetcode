// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

#include <functional>

// JavaScript problem; C++ stand-in.
class Solution {
public:
    std::function<int()> createCounter(int n) {
        return [cur = n]() mutable {
            return cur++;
        };
    }
};
