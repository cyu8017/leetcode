// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

import java.util.function.IntSupplier;

// JS generator stand-in
class Solution {
    public IntSupplier fibGenerator() {
        int[] ab = new int[] {0, 1};
        return () -> {
            int v = ab[0];
            int na = ab[1];
            ab[1] = ab[0] + ab[1];
            ab[0] = na;
            return v;
        };
    }
}
