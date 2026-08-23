// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

import java.util.function.IntBinaryOperator;

// JavaScript problem; Java stand-in.
class Solution {
    public int[] map(int[] arr, IntBinaryOperator fn) {
        int[] out = new int[arr.length];
        for (int i = 0; i < arr.length; i++) out[i] = fn.applyAsInt(arr[i], i);
        return out;
    }
}
