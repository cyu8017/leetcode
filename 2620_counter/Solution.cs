// LeetCode 2620 - Counter
// https://leetcode.com/problems/counter/

// JavaScript problem; C# stand-in.
using System;

public class Solution {
    public Func<int> CreateCounter(int n) {
        int cur = n;
        return () => cur++;
    }
}
