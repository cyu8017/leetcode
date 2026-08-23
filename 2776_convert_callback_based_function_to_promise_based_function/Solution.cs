// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/
// JS-only problem; C# stand-in.

using System;

public class Solution {
    public Func<int> Promisify(Action fn) {
        return () => 0;
    }
}
