// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

public class Solution {
    public int[] RestoreArray(int[][] adjacentPairs) {
        var graph = new Dictionary<int, List<int>>();
        foreach (var pair in adjacentPairs) {
            if (!graph.ContainsKey(pair[0])) {
                graph[pair[0]] = new List<int>();
            }
            if (!graph.ContainsKey(pair[1])) {
                graph[pair[1]] = new List<int>();
            }
            graph[pair[0]].Add(pair[1]);
            graph[pair[1]].Add(pair[0]);
        }
        int start = 0;
        foreach (var pair in adjacentPairs) {
            if (graph[pair[0]].Count == 1) {
                start = pair[0];
                break;
            }
            if (graph[pair[1]].Count == 1) {
                start = pair[1];
                break;
            }
        }
        int n = graph.Count;
        var ans = new int[n];
        ans[0] = start;
        int? prev = null;
        for (int i = 1; i < n; i++) {
            int cur = ans[i - 1];
            var neighbors = graph[cur];
            ans[i] = neighbors[0] != prev ? neighbors[0] : neighbors[1];
            prev = cur;
        }
        return ans;
    }
}
