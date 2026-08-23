// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumDistance(int[][] points) {
        var st1 = new SortedDictionary<int, int>();
        var st2 = new SortedDictionary<int, int>();
        void Merge(SortedDictionary<int, int> st, int x, int v) {
            if (!st.ContainsKey(x)) st[x] = 0;
            st[x] += v;
            if (st[x] == 0) st.Remove(x);
        }
        foreach (var p in points) {
            Merge(st1, p[0] + p[1], 1);
            Merge(st2, p[0] - p[1], 1);
        }
        int ans = int.MaxValue;
        foreach (var p in points) {
            int x = p[0], y = p[1];
            Merge(st1, x + y, -1);
            Merge(st2, x - y, -1);
            int a = First(st1), b = Last(st1), c = First(st2), d = Last(st2);
            ans = Math.Min(ans, Math.Max(b - a, d - c));
            Merge(st1, x + y, 1);
            Merge(st2, x - y, 1);
        }
        return ans;
    }

    static int First(SortedDictionary<int, int> st) {
        foreach (var kv in st) return kv.Key;
        return 0;
    }

    static int Last(SortedDictionary<int, int> st) {
        int last = 0;
        foreach (var kv in st) last = kv.Key;
        return last;
    }
}
