// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

// JavaScript problem; C# stand-in (no real timeout).
using System;

public class Solution {
    public Func<int> TimeLimit(Func<int> fn, int t) {
        return () => fn();
    }
}
