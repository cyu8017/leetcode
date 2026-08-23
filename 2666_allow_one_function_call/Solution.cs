// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

// JS once stand-in
using System;

public class Solution {
    public Func<int, int?> Once(Func<int, int> fn) {
        bool called = false;
        int res = 0;
        return arg => {
            if (called) return null;
            called = true;
            res = fn(arg);
            return res;
        };
    }
}
