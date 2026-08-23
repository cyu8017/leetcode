// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

// JavaScript problem; C# stand-in.
using System;

public class Solution {
    public int Reduce(int[] nums, Func<int, int, int> fn, int init) {
        int acc = init;
        foreach (int x in nums) acc = fn(acc, x);
        return acc;
    }
}
