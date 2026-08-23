// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

// JavaScript problem; C# stand-in.
using System;

public class Solution {
    public int[] Map(int[] arr, Func<int, int, int> fn) {
        int[] outArr = new int[arr.Length];
        for (int i = 0; i < arr.Length; i++) outArr[i] = fn(arr[i], i);
        return outArr;
    }
}
