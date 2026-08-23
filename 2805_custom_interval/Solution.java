// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/
// JS-only problem; C# stand-in returning a cancel flag setter.

class Solution {
    public Action customInterval(Action fn, int delay, int period) {
        boolean cancelled = false;
        return () -> { cancelled = true; };
    }
}
