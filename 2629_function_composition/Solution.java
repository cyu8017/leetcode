// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

import java.util.*;
import java.util.function.IntUnaryOperator;

// JavaScript problem; Java stand-in.
class Solution {
    public IntUnaryOperator compose(List<IntUnaryOperator> functions) {
        return x -> {
            for (int i = functions.size() - 1; i >= 0; i--) x = functions.get(i).applyAsInt(x);
            return x;
        };
    }
}
