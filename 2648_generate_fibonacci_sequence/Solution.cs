// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

// JS generator stand-in
using System;

public class Solution {
    public Func<int> FibGenerator() {
        int a = 0, b = 1;
        return () => {
            int v = a;
            int na = b;
            b = a + b;
            a = na;
            return v;
        };
    }
}
