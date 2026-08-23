// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

import java.util.function.IntBinaryOperator;

// JavaScript problem; Java stand-in.
class Solution {
    public int reduce(int[] nums, IntBinaryOperator fn, int init) {
        int acc = init;
        for (int x : nums) acc = fn.applyAsInt(acc, x);
        return acc;
    }
}
