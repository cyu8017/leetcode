// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public string SmallestStringWithSwaps(string s, int[][] pairs) {
        int n = s.Length;
        var parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int x) {
            while (x != parent[x]) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        foreach (var p in pairs) {
            int ra = Find(p[0]), rb = Find(p[1]);
            parent[ra] = rb;
        }

        var groups = new Dictionary<int, List<char>>();
        for (int i = 0; i < n; i++) {
            int root = Find(i);
            if (!groups.ContainsKey(root)) groups[root] = new List<char>();
            groups[root].Add(s[i]);
        }
        foreach (var kv in groups) kv.Value.Sort((a, b) => b.CompareTo(a));

        var sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            var list = groups[Find(i)];
            char ch = list[^1];
            list.RemoveAt(list.Count - 1);
            sb.Append(ch);
        }
        return sb.ToString();
    }
}
