// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

using System;
using System.Collections.Generic;

public class Solution {
    public int NumSquarefulPerms(int[] nums) {
        var count = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        var graph = new Dictionary<int, List<int>>();
        foreach (var a in count.Keys) graph[a] = new List<int>();
        foreach (var a in count.Keys) {
            foreach (var b in count.Keys) {
                long s = (long)a + b;
                long r = (long)Math.Round(Math.Sqrt(s));
                if (r * r == s) graph[a].Add(b);
            }
        }
        int ans = 0;
        void Dfs(int x, int remain) {
            if (remain == 0) { ans++; return; }
            foreach (int y in graph[x]) {
                if (count[y] > 0) {
                    count[y]--;
                    Dfs(y, remain - 1);
                    count[y]++;
                }
            }
        }
        var keys = new List<int>(count.Keys);
        foreach (int x in keys) {
            count[x]--;
            Dfs(x, nums.Length - 1);
            count[x]++;
        }
        return ans;
    }
}
