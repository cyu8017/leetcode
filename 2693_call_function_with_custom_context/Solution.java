// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

import java.util.function.IntBinaryOperator;

// JS call stand-in
class Solution {
    public int call(IntBinaryOperator fn, int ctx, int arg) {
        return fn.applyAsInt(ctx, arg);
    }
}
