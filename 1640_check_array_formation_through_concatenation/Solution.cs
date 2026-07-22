// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

using System.Collections.Generic;

public class Solution {
    public bool CanFormArray(int[] arr, int[][] pieces) {
        var byFirst = new Dictionary<int, int[]>();
        foreach (var p in pieces) byFirst[p[0]] = p;
        int i = 0;
        while (i < arr.Length) {
            if (!byFirst.TryGetValue(arr[i], out var p)) return false;
            for (int j = 0; j < p.Length; j++) {
                if (i + j >= arr.Length || arr[i + j] != p[j]) return false;
            }
            i += p.Length;
        }
        return true;
    }
}
