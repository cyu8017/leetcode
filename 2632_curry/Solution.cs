// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

// JavaScript problem; C# stand-in applying all args at once.
using System;

public class Solution {
    public Func<int[], int> Curry(Func<int[], int> fn, int arity) {
        return args => fn(args);
    }
}
