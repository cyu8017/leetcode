// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/
// JS-only problem; C# stand-in.

using System;

public class Solution {
    public void ForEach(int[] arr, Action<int, int, int[]> callback) {
        for (int i = 0; i < arr.Length; i++) callback(arr[i], i, arr);
    }
}
