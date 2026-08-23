// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

#include <functional>

class Solution {
public:
    // JS generator stand-in
    std::function<int()> fibGenerator() {
        int a = 0, b = 1;
        return [a, b]() mutable {
            int v = a;
            int na = b;
            b = a + b;
            a = na;
            return v;
        };
    }
};
