// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

import java.util.function.IntSupplier;

// JavaScript problem; Java stand-in.
class Solution {
    public IntSupplier createCounter(int n) {
        int[] cur = new int[] {n};
        return () -> cur[0]++;
    }
}
