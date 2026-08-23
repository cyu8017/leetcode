// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

import java.util.function.Function;

// JavaScript problem; Java stand-in applying all args at once.
class Solution {
    public Function<int[], Integer> curry(Function<int[], Integer> fn, int arity) {
        return args -> fn.apply(args);
    }
}
