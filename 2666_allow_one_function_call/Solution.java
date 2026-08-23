// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

import java.util.function.IntUnaryOperator;
import java.util.function.IntFunction;

// JS once stand-in
class Solution {
    public IntFunction<Integer> once(IntUnaryOperator fn) {
        boolean[] called = new boolean[] {false};
        int[] res = new int[] {0};
        return arg -> {
            if (called[0]) return null;
            called[0] = true;
            res[0] = fn.applyAsInt(arg);
            return res[0];
        };
    }
}
