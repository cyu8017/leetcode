// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

// JS call stand-in
using System;

public class Solution {
    public int Call(Func<int, int, int> fn, int ctx, int arg) {
        return fn(ctx, arg);
    }
}
