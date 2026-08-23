// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

// JavaScript problem; C# stand-in.
using System;
using System.Collections.Generic;

public class Solution {
    public int[] Filter(int[] arr, Func<int, int, bool> fn) {
        var outList = new List<int>();
        for (int i = 0; i < arr.Length; i++) {
            if (fn(arr[i], i)) outList.Add(arr[i]);
        }
        return outList.ToArray();
    }
}
