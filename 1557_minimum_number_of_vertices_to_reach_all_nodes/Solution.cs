// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

using System.Collections.Generic;

public class Solution {
    public IList<int> FindSmallestSetOfVertices(int n, IList<IList<int>> edges) {
        var incoming = new bool[n];
        foreach (var e in edges) incoming[e[1]] = true;
        var result = new List<int>();
        for (int v = 0; v < n; v++)
            if (!incoming[v]) result.Add(v);
        return result;
    }
}
