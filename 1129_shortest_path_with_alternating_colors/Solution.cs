// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

using System.Collections.Generic;

public class Solution {
    public int[] ShortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        var red = new List<int>[n];
        var blue = new List<int>[n];
        for (int i = 0; i < n; i++) {
            red[i] = new List<int>();
            blue[i] = new List<int>();
        }
        foreach (var e in redEdges) red[e[0]].Add(e[1]);
        foreach (var e in blueEdges) blue[e[0]].Add(e[1]);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        var seen = new bool[n, 2];
        var q = new Queue<(int node, int color, int dist)>();
        q.Enqueue((0, 0, 0));
        q.Enqueue((0, 1, 0));
        seen[0, 0] = seen[0, 1] = true;
        while (q.Count > 0) {
            var (node, color, dist) = q.Dequeue();
            if (ans[node] == -1) ans[node] = dist;
            var nextEdges = color == 0 ? red[node] : blue[node];
            int nextColor = 1 - color;
            foreach (int nxt in nextEdges) {
                if (!seen[nxt, nextColor]) {
                    seen[nxt, nextColor] = true;
                    q.Enqueue((nxt, nextColor, dist + 1));
                }
            }
        }
        return ans;
    }
}
