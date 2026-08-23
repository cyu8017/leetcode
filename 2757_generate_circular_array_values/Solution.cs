// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/
// JS generator stand-in.

using System;

public class Solution {
    public Func<int> CyclicGenerator(int[] arr, int startIndex) {
        int i = startIndex;
        int n = arr.Length;
        return () => {
            int v = arr[i];
            i = (i + 1) % n;
            return v;
        };
    }
}
