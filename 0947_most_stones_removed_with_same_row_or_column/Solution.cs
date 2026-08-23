// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

using System.Collections.Generic;

public class Solution {
    public int RemoveStones(int[][] stones) {
        var parent = new Dictionary<int, int>();
        int Find(int x) {
            if (!parent.ContainsKey(x)) parent[x] = x;
            return parent[x] == x ? x : parent[x] = Find(parent[x]);
        }
        void Unite(int a, int b) { parent[Find(a)] = Find(b); }
        foreach (var s in stones) Unite(s[0], ~s[1]);
        var roots = new HashSet<int>();
        foreach (var s in stones) roots.Add(Find(s[0]));
        return stones.Length - roots.Count;
    }
}
