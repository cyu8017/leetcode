// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

// JavaScript problem; C# stand-in (immediate invoke; no timer runtime).
using System;

public class Solution {
    public Action Debounce(Action fn, int t) {
        return () => fn();
    }
}
