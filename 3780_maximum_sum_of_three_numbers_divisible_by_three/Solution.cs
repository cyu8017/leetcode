// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumSum(int[] nums) {
        Array.Sort(nums);
        var g = new List<int>[3];
        for (int i = 0; i < 3; i++) g[i] = new List<int>();
        foreach (int x in nums) g[x % 3].Add(x);
        int ans = 0;
        for (int a = 0; a < 3; a++) {
            if (g[a].Count > 0) {
                int x = g[a][g[a].Count - 1];
                g[a].RemoveAt(g[a].Count - 1);
                for (int b = 0; b < 3; b++) {
                    if (g[b].Count > 0) {
                        int y = g[b][g[b].Count - 1];
                        g[b].RemoveAt(g[b].Count - 1);
                        int c = (3 - (a + b) % 3) % 3;
                        if (g[c].Count > 0) {
                            int z = g[c][g[c].Count - 1];
                            ans = Math.Max(ans, x + y + z);
                        }
                        g[b].Add(y);
                    }
                }
                g[a].Add(x);
            }
        }
        return ans;
    }
}
