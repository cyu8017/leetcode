// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

using System;
using System.Collections.Generic;

public class Solution {
    public int MctFromLeafValues(int[] arr) {
        var stack = new List<int> { int.MaxValue };
        int ans = 0;
        foreach (int x in arr) {
            while (stack[stack.Count - 1] <= x) {
                int mid = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                ans += mid * Math.Min(stack[stack.Count - 1], x);
            }
            stack.Add(x);
        }
        while (stack.Count > 2) {
            int mid = stack[stack.Count - 1];
            stack.RemoveAt(stack.Count - 1);
            ans += mid * stack[stack.Count - 1];
        }
        return ans;
    }
}
