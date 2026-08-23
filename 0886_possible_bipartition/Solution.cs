// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

using System.Collections.Generic;

public class Solution {
    public bool PossibleBipartition(int n, int[][] dislikes) {
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        foreach (var e in dislikes) {
            graph[e[0]].Add(e[1]);
            graph[e[1]].Add(e[0]);
        }
        var color = new Dictionary<int, int>();
        for (int start = 1; start <= n; start++) {
            if (color.ContainsKey(start)) continue;
            var queue = new Queue<int>();
            queue.Enqueue(start);
            color[start] = 0;
            while (queue.Count > 0) {
                int node = queue.Dequeue();
                foreach (int nei in graph[node]) {
                    if (!color.ContainsKey(nei)) {
                        color[nei] = color[node] ^ 1;
                        queue.Enqueue(nei);
                    } else if (color[nei] == color[node]) return false;
                }
            }
        }
        return true;
    }
}
