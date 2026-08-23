// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> PancakeSort(int[] arr) {
        int[] a = (int[])arr.Clone();
        var ans = new List<int>();
        for (int size = a.Length; size > 1; size--) {
            int i = Array.IndexOf(a, size);
            if (i == size - 1) continue;
            if (i > 0) {
                ans.Add(i + 1);
                Array.Reverse(a, 0, i + 1);
            }
            ans.Add(size);
            Array.Reverse(a, 0, size);
        }
        return ans;
    }
}
