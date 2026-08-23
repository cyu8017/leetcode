// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

using System.Collections.Generic;

public class Solution {
    public int[][] Chunk(int[] arr, int size) {
        var ans = new List<int[]>();
        for (int i = 0; i < arr.Length; i += size) {
            var part = new List<int>();
            for (int j = i; j < arr.Length && j < i + size; j++) part.Add(arr[j]);
            ans.Add(part.ToArray());
        }
        return ans.ToArray();
    }
}
