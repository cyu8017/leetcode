// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

import java.util.function.IntSupplier;

// JavaScript problem; Java stand-in (no real timeout).
class Solution {
    public IntSupplier timeLimit(IntSupplier fn, int t) {
        return () -> fn.getAsInt();
    }
}
