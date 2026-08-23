// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

#include <functional>

class Solution {
public:
    // JS call stand-in
    int call(std::function<int(int, int)> fn, int ctx, int arg) {
        (void)ctx;
        return fn(ctx, arg);
    }
};
