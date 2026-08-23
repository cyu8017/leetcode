// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

// JavaScript problem; C# stand-in (sequential execution).
using System;
using System.Collections.Generic;

public class Solution {
    public int[] PromisePool(IList<Func<int>> functions, int n) {
        int[] ans = new int[functions.Count];
        for (int i = 0; i < functions.Count; i++) ans[i] = functions[i]();
        return ans;
    }
}
