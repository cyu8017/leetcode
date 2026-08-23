// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/
// JS-only problem; C# stand-in returning a cancel flag setter.

using System;

public class Solution {
    public Action CustomInterval(Action fn, int delay, int period) {
        bool cancelled = false;
        return () => { cancelled = true; };
    }
}
